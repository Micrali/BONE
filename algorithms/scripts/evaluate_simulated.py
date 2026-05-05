import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / 'algorithms'))

from bonevibauth.pipeline import BoneVibAuthPipeline
from bonevibauth.signal_processing import generate_chirp
from simulate_dataset import synthesize_hcr


def main():
    pipeline = BoneVibAuthPipeline({'TEMPLATE_DIR': ROOT / 'data' / 'templates', 'AUTH_THRESHOLD': 0.65})
    probe = generate_chirp()
    users = 10
    enroll_count = 10
    test_count = 5

    for user in range(users):
        features = [pipeline.extract_feature(synthesize_hcr(user * 100 + i, probe)) for i in range(enroll_count)]
        pipeline.save_template(f'user_{user:02d}', pipeline.build_template(features))

    genuine_accept = 0
    genuine_total = 0
    impostor_accept = 0
    impostor_total = 0

    for user in range(users):
        for i in range(test_count):
            feature = pipeline.extract_feature(synthesize_hcr(user * 100 + enroll_count + i, probe))
            result = pipeline.verify(f'user_{user:02d}', feature)
            genuine_accept += int(result['accepted'])
            genuine_total += 1

        for attacker in range(users):
            if attacker == user:
                continue
            feature = pipeline.extract_feature(synthesize_hcr(attacker * 100 + 90, probe))
            result = pipeline.verify(f'user_{user:02d}', feature)
            impostor_accept += int(result['accepted'])
            impostor_total += 1

    tar = genuine_accept / genuine_total
    frr = 1 - tar
    far = impostor_accept / impostor_total
    trr = 1 - far
    bac = (tar + trr) / 2

    print({
        'BAC': round(bac * 100, 2),
        'FAR': round(far * 100, 2),
        'FRR': round(frr * 100, 2),
        'genuine_total': genuine_total,
        'impostor_total': impostor_total,
    })


if __name__ == '__main__':
    main()
