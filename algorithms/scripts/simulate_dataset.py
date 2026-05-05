import argparse
from pathlib import Path
import numpy as np

from bonevibauth.signal_processing import generate_chirp


def synthesize_hcr(user_index, probe, noise=0.035):
    rng = np.random.default_rng(user_index)
    resonance = 1 + 0.12 * np.sin(np.linspace(0, np.pi * (2 + user_index % 5), len(probe)))
    phase = np.roll(probe, user_index % 11)
    anatomy = 0.7 * probe + 0.3 * phase
    return (anatomy * resonance + rng.normal(0, noise, len(probe))).astype(np.float32)


def main():
    parser = argparse.ArgumentParser(description='Generate simulated HCR samples for BoneVibAuth')
    parser.add_argument('--users', type=int, default=10)
    parser.add_argument('--samples', type=int, default=10)
    parser.add_argument('--out', default='data/simulated')
    args = parser.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    probe = generate_chirp()
    np.save(out_dir / 'chirp_probe.npy', probe)

    for user in range(args.users):
        user_dir = out_dir / f'user_{user:02d}'
        user_dir.mkdir(exist_ok=True)
        for sample in range(args.samples):
            hcr = synthesize_hcr(user * 100 + sample, probe)
            np.save(user_dir / f'hcr_{sample:02d}.npy', hcr)

    print(f'Generated {args.users * args.samples} samples in {out_dir}')


if __name__ == '__main__':
    main()
