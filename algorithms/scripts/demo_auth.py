import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[2]
sys.path.append(str(ROOT / 'algorithms'))

from bonevibauth.pipeline import BoneVibAuthPipeline
from bonevibauth.signal_processing import generate_chirp


def synthesize_response(seed, probe):
    rng = np.random.default_rng(seed)
    response = 0.78 * probe + 0.22 * np.roll(probe, seed % 13)
    response += rng.normal(0, 0.035, len(probe))
    return response.astype(np.float32)


def main():
    pipeline = BoneVibAuthPipeline({'TEMPLATE_DIR': ROOT / 'data' / 'templates'})
    probe = generate_chirp()
    enroll_features = [pipeline.extract_feature(synthesize_response(i, probe)) for i in range(10)]
    template = pipeline.build_template(enroll_features)
    pipeline.save_template('demo-user', template)

    claimed = pipeline.extract_feature(synthesize_response(2, probe))
    impostor = pipeline.extract_feature(synthesize_response(99, probe))

    print('genuine:', pipeline.verify('demo-user', claimed))
    print('impostor:', pipeline.verify('demo-user', impostor))


if __name__ == '__main__':
    main()
