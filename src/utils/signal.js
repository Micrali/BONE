export function generateChirp(sampleRate = 467, lowHz = 50, highHz = 850, seconds = 1.5) {
  const length = Math.floor(sampleRate * seconds);
  return Array.from({ length }, (_, index) => {
    const t = index / sampleRate;
    const k = (highHz - lowHz) / seconds;
    const phase = 2 * Math.PI * (lowHz * t + 0.5 * k * t * t);
    return Math.sin(phase);
  });
}

function seededNoise(seed) {
  let value = seed % 2147483647;
  if (value <= 0) value += 2147483646;
  return () => {
    value = (value * 16807) % 2147483647;
    return (value - 1) / 2147483646;
  };
}

export function synthesizeHcrSignal(seed = 1, options = {}) {
  const sampleRate = options.sampleRate || 467;
  const probe = generateChirp(sampleRate, options.lowHz || 50, options.highHz || 850, options.seconds || 1.5);
  const random = seededNoise(seed + 17);
  const shift = seed % 13;
  return probe.map((value, index) => {
    const shifted = probe[(index + shift) % probe.length];
    const resonance = 1 + 0.12 * Math.sin((Math.PI * (2 + (seed % 5)) * index) / probe.length);
    const noise = (random() - 0.5) * 0.07;
    return Number(((0.78 * value + 0.22 * shifted) * resonance + noise).toFixed(6));
  });
}

export function buildEnrollmentSignals(seedBase = 1, count = 10) {
  return Array.from({ length: count }, (_, index) => synthesizeHcrSignal(seedBase + index));
}
