# Generated for BoneVibAuth project scaffold

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('external_id', models.CharField(max_length=64, unique=True)),
                ('display_name', models.CharField(blank=True, max_length=128)),
                ('device_model', models.CharField(blank=True, max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='HCRSample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.CharField(choices=[('enroll', 'Enroll'), ('verify', 'Verify'), ('attack', 'Attack')], max_length=16)),
                ('sample_rate', models.PositiveIntegerField(default=467)),
                ('duration_seconds', models.FloatField(default=1.5)),
                ('raw_signal', models.JSONField(help_text='采集的 HCR/IMU 一维或多轴信号序列')),
                ('feature_vector', models.JSONField(blank=True, default=list)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='samples', to='authentication.subject')),
            ],
        ),
        migrations.CreateModel(
            name='AuthSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(default=0)),
                ('threshold', models.FloatField(default=0.65)),
                ('accepted', models.BooleanField(default=False)),
                ('far_estimate', models.FloatField(default=0)),
                ('frr_estimate', models.FloatField(default=0)),
                ('latency_ms', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auth_sessions', to='authentication.subject')),
            ],
        ),
    ]
