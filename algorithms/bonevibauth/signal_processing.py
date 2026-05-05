import numpy as np
from scipy import signal


def generate_chirp(sample_rate=467, low_hz=50.0, high_hz=850.0, duration_seconds=1.5, amplitude=1.0):
    """生成作品书中的短时 Chirp 探测信号。"""
    t = np.linspace(0, duration_seconds, int(sample_rate * duration_seconds), endpoint=False)
    # 受限采样率下会出现混叠，保留作品书中的低采样率模拟特征。
    return amplitude * signal.chirp(t, f0=low_hz, f1=high_hz, t1=duration_seconds, method='linear')


def normalize(values):
    arr = np.asarray(values, dtype=np.float32)
    if arr.size == 0:
        return arr
    return (arr - np.mean(arr)) / (np.std(arr) + 1e-8)


def bandpass_filter(values, sample_rate, low_hz=1.0, high_hz=None, order=4):
    arr = normalize(values)
    nyquist = sample_rate / 2
    if high_hz is None or high_hz >= nyquist:
        high_hz = nyquist * 0.95
    low_hz = max(low_hz, 0.1)
    sos = signal.butter(order, [low_hz / nyquist, high_hz / nyquist], btype='band', output='sos')
    return signal.sosfiltfilt(sos, arr).astype(np.float32)


def estimate_frequency_response(input_signal, output_signal, sample_rate, nperseg=128):
    """根据 H(f)=P_yx(f)/P_xx(f) 估计头部接触响应频响。"""
    x = normalize(input_signal)
    y = normalize(output_signal)
    nperseg = min(nperseg, len(x), len(y))
    freqs, pxx = signal.welch(x, fs=sample_rate, nperseg=nperseg)
    _, pyx = signal.csd(y, x, fs=sample_rate, nperseg=nperseg)
    response = pyx / (pxx + 1e-8)
    magnitude = np.abs(response)
    return freqs.astype(np.float32), normalize(magnitude).astype(np.float32)


def segment_signal(values, frame_size=96, hop_size=48):
    arr = normalize(values)
    if len(arr) < frame_size:
        padded = np.pad(arr, (0, frame_size - len(arr)))
        return np.asarray([padded], dtype=np.float32)
    frames = []
    for start in range(0, len(arr) - frame_size + 1, hop_size):
        frames.append(arr[start:start + frame_size])
    return np.asarray(frames, dtype=np.float32)
