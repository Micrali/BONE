from django.db import models


class Subject(models.Model):
    external_id = models.CharField(max_length=64, unique=True)
    display_name = models.CharField(max_length=128, blank=True)
    device_model = models.CharField(max_length=128, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.external_id


class HCRSample(models.Model):
    PURPOSE_CHOICES = [
        ('enroll', 'Enroll'),
        ('verify', 'Verify'),
        ('attack', 'Attack'),
    ]

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='samples')
    purpose = models.CharField(max_length=16, choices=PURPOSE_CHOICES)
    sample_rate = models.PositiveIntegerField(default=467)
    duration_seconds = models.FloatField(default=1.5)
    raw_signal = models.JSONField(help_text='采集的 HCR/IMU 一维或多轴信号序列')
    feature_vector = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class AuthSession(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='auth_sessions')
    score = models.FloatField(default=0)
    threshold = models.FloatField(default=0.65)
    accepted = models.BooleanField(default=False)
    far_estimate = models.FloatField(default=0)
    frr_estimate = models.FloatField(default=0)
    latency_ms = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
