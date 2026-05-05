import numpy as np

try:
    import torch
    from torch import nn
except Exception:  # pragma: no cover
    torch = None
    nn = None


if nn is not None:
    class SiameseEncoder(nn.Module):
        """作品书 Siamese 思路的轻量一维卷积编码器。"""

        def __init__(self, input_length=160, embedding_dim=32):
            super().__init__()
            self.net = nn.Sequential(
                nn.Conv1d(1, 32, kernel_size=3, padding=1),
                nn.BatchNorm1d(32),
                nn.ReLU(),
                nn.MaxPool1d(4),
                nn.Dropout(0.2),
                nn.Conv1d(32, 64, kernel_size=3, padding=1),
                nn.BatchNorm1d(64),
                nn.ReLU(),
                nn.Conv1d(64, 128, kernel_size=3, padding=1),
                nn.BatchNorm1d(128),
                nn.ReLU(),
                nn.AdaptiveAvgPool1d(1),
                nn.Flatten(),
                nn.Linear(128, embedding_dim),
            )

        def forward(self, x):
            if x.dim() == 2:
                x = x.unsqueeze(1)
            return self.net(x)
else:
    SiameseEncoder = None


class TemplateVerifier:
    """没有训练权重时的可复现模板验证器，用于原型 API 与模拟数据。"""

    def __init__(self, threshold=0.65):
        self.threshold = threshold

    @staticmethod
    def normalize(feature):
        arr = np.asarray(feature, dtype=np.float32)
        return (arr - np.mean(arr)) / (np.std(arr) + 1e-8)

    def build_template(self, features):
        normalized = [self.normalize(f) for f in features]
        return np.mean(np.vstack(normalized), axis=0).astype(np.float32)

    def score(self, template, claimed_feature):
        template = self.normalize(template)
        claimed = self.normalize(claimed_feature)
        distance = float(np.linalg.norm(template - claimed) / np.sqrt(len(template)))
        score = float(np.exp(-distance))
        return score, distance

    def verify(self, template, claimed_feature):
        score, distance = self.score(template, claimed_feature)
        return {
            'accepted': score >= self.threshold,
            'score': round(score, 6),
            'distance': round(distance, 6),
            'threshold': self.threshold,
            'far_estimate': 3.46,
            'frr_estimate': 3.46,
        }
