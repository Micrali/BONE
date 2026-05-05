import time
from django.conf import settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from algorithms.bonevibauth.pipeline import BoneVibAuthPipeline
from .models import AuthSession, HCRSample, Subject
from .serializers import EnrollmentSerializer, VerificationSerializer

pipeline = BoneVibAuthPipeline(settings.BONEVIBAUTH)


@api_view(['GET'])
@permission_classes([AllowAny])
def health(request):
    return Response({
        'status': 'ok',
        'system': 'BoneVibAuth',
        'core': ['Chirp excitation', 'HCR capture', 'MFCC feature', 'Siamese verifier'],
    })


@api_view(['GET'])
@permission_classes([AllowAny])
def chirp_config(request):
    cfg = settings.BONEVIBAUTH
    return Response({
        'sample_rate': cfg['SAMPLE_RATE'],
        'low_hz': cfg['CHIRP_LOW_HZ'],
        'high_hz': cfg['CHIRP_HIGH_HZ'],
        'duration_seconds': cfg['CHIRP_SECONDS'],
        'samples': pipeline.generate_probe().round(6).tolist(),
    })


@api_view(['POST'])
def enroll(request):
    serializer = EnrollmentSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data

    subject, _ = Subject.objects.update_or_create(
        external_id=data['external_id'],
        defaults={
            'display_name': data.get('display_name', ''),
            'device_model': data.get('device_model', ''),
        },
    )

    feature_vectors = []
    for signal in data['signals']:
        features = pipeline.extract_feature(signal, sample_rate=data['sample_rate'])
        feature_vectors.append(features.tolist())
        HCRSample.objects.create(
            subject=subject,
            purpose='enroll',
            sample_rate=data['sample_rate'],
            raw_signal=signal,
            feature_vector=features.tolist(),
        )

    template = pipeline.build_template(feature_vectors)
    pipeline.save_template(data['external_id'], template)

    return Response({
        'subject': data['external_id'],
        'template_size': len(feature_vectors),
        'embedding_dim': len(template),
        'message': '用户 HCR 注册模板已生成',
    }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def verify(request):
    started = time.perf_counter()
    serializer = VerificationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    data = serializer.validated_data

    try:
        subject = Subject.objects.get(external_id=data['external_id'])
    except Subject.DoesNotExist:
        return Response({'detail': 'subject not enrolled'}, status=status.HTTP_404_NOT_FOUND)

    features = pipeline.extract_feature(data['claimed_signal'], sample_rate=data['sample_rate'])
    result = pipeline.verify(data['external_id'], features)
    latency_ms = (time.perf_counter() - started) * 1000

    HCRSample.objects.create(
        subject=subject,
        purpose='verify',
        sample_rate=data['sample_rate'],
        raw_signal=data['claimed_signal'],
        feature_vector=features.tolist(),
    )
    session = AuthSession.objects.create(
        subject=subject,
        score=result['score'],
        threshold=result['threshold'],
        accepted=result['accepted'],
        far_estimate=result['far_estimate'],
        frr_estimate=result['frr_estimate'],
        latency_ms=latency_ms,
    )

    return Response({
        'session_id': session.id,
        'subject': data['external_id'],
        'accepted': result['accepted'],
        'score': result['score'],
        'distance': result['distance'],
        'threshold': result['threshold'],
        'latency_ms': round(latency_ms, 2),
    })


@api_view(['GET'])
@permission_classes([AllowAny])
def metrics(request):
    total_sessions = AuthSession.objects.count()
    accepted_sessions = AuthSession.objects.filter(accepted=True).count()
    recent_sessions = AuthSession.objects.order_by('-created_at')[:8]
    avg_latency = 0
    if total_sessions:
        avg_latency = sum(item.latency_ms for item in AuthSession.objects.all()) / total_sessions

    return Response({
        'paper_metrics': {
            'bac': 96.55,
            'far': 3.46,
            'frr': 3.46,
            'training_samples_per_user': 10,
            'collection_seconds': 15,
            'auth_latency_ms': 54.05,
        },
        'runtime_metrics': {
            'subjects': Subject.objects.count(),
            'samples': HCRSample.objects.count(),
            'sessions': total_sessions,
            'accepted_sessions': accepted_sessions,
            'acceptance_rate': round(accepted_sessions / total_sessions, 4) if total_sessions else 0,
            'avg_latency_ms': round(avg_latency, 2),
        },
        'recent_sessions': [
            {
                'subject': item.subject.external_id,
                'score': item.score,
                'accepted': item.accepted,
                'latency_ms': round(item.latency_ms, 2),
                'created_at': item.created_at.isoformat(),
            }
            for item in recent_sessions
        ],
        'robustness': {
            'BMI_attack_far': 0.32,
            'BFR_attack_far': 0.08,
            'SMR_attack_far': 1.92,
        },
    })
