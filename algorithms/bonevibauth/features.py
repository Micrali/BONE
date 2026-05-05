import numpy as np
import librosa

from .signal_processing import bandpass_filter, estimate_frequency_response


def extract_mfcc(signal_values, sample_rate, n_mfcc=24):
    filtered = bandpass_filter(signal_values, sample_rate)
    mfcc = librosa.feature.mfcc(y=filtered.astype(np.float32), sr=sample_rate, n_mfcc=n_mfcc)
    delta = librosa.feature.delta(mfcc)
    delta2 = librosa.feature.delta(mfcc, order=2)
    feature = np.concatenate([
        np.mean(mfcc, axis=1),
        np.std(mfcc, axis=1),
        np.mean(delta, axis=1),
        np.mean(delta2, axis=1),
    ])
    return feature.astype(np.float32)


def extract_hcr_feature(probe_signal, response_signal, sample_rate):
    _, freq_response = estimate_frequency_response(probe_signal, response_signal, sample_rate)
    mfcc_feature = extract_mfcc(response_signal, sample_rate)
    feature = np.concatenate([freq_response[:64], mfcc_feature])
    return feature.astype(np.float32)
