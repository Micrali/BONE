from pathlib import Path
import joblib
import numpy as np

from .features import extract_hcr_feature, extract_mfcc
from .signal_processing import generate_chirp
from .siamese import TemplateVerifier


class BoneVibAuthPipeline:
    """BoneVibAuth 核心流程：Chirp -> HCR -> MFCC/频响 -> Siamese/模板验证。"""

    def __init__(self, config=None):
        self.config = config or {}
        self.sample_rate = int(self.config.get('SAMPLE_RATE', 467))
        self.low_hz = float(self.config.get('CHIRP_LOW_HZ', 50))
        self.high_hz = float(self.config.get('CHIRP_HIGH_HZ', 850))
        self.duration_seconds = float(self.config.get('CHIRP_SECONDS', 1.5))
        self.template_dir = Path(self.config.get('TEMPLATE_DIR', 'data/templates'))
        self.template_dir.mkdir(parents=True, exist_ok=True)
        self.verifier = TemplateVerifier(float(self.config.get('AUTH_THRESHOLD', 0.65)))

    def generate_probe(self):
        return generate_chirp(
            sample_rate=self.sample_rate,
            low_hz=self.low_hz,
            high_hz=self.high_hz,
            duration_seconds=self.duration_seconds,
        )

    def extract_feature(self, response_signal, sample_rate=None):
        sample_rate = sample_rate or self.sample_rate
        probe = generate_chirp(sample_rate, self.low_hz, self.high_hz, self.duration_seconds)
        response = np.asarray(response_signal, dtype=np.float32)
        if len(response) == len(probe):
            return extract_hcr_feature(probe, response, sample_rate)
        return extract_mfcc(response, sample_rate)

    def build_template(self, feature_vectors):
        return self.verifier.build_template(feature_vectors)

    def template_path(self, external_id):
        safe_id = ''.join(ch for ch in external_id if ch.isalnum() or ch in ('-', '_'))
        return self.template_dir / f'{safe_id}.joblib'

    def save_template(self, external_id, template):
        joblib.dump(np.asarray(template, dtype=np.float32), self.template_path(external_id))

    def load_template(self, external_id):
        path = self.template_path(external_id)
        if not path.exists():
            raise FileNotFoundError(f'No template for {external_id}')
        return joblib.load(path)

    def verify(self, external_id, claimed_feature):
        template = self.load_template(external_id)
        return self.verifier.verify(template, claimed_feature)
