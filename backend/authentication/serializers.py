from rest_framework import serializers
from .models import AuthSession, HCRSample, Subject


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['id', 'external_id', 'display_name', 'device_model', 'created_at']


class EnrollmentSerializer(serializers.Serializer):
    external_id = serializers.CharField(max_length=64)
    display_name = serializers.CharField(max_length=128, required=False, allow_blank=True)
    device_model = serializers.CharField(max_length=128, required=False, allow_blank=True)
    sample_rate = serializers.IntegerField(default=467)
    signals = serializers.ListField(
        child=serializers.ListField(child=serializers.FloatField()), min_length=1
    )


class VerificationSerializer(serializers.Serializer):
    external_id = serializers.CharField(max_length=64)
    claimed_signal = serializers.ListField(child=serializers.FloatField(), min_length=1)
    sample_rate = serializers.IntegerField(default=467)


class AuthSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthSession
        fields = ['id', 'subject', 'score', 'threshold', 'accepted', 'far_estimate', 'frr_estimate', 'latency_ms', 'created_at']


class HCRSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HCRSample
        fields = ['id', 'subject', 'purpose', 'sample_rate', 'duration_seconds', 'raw_signal', 'feature_vector', 'created_at']
