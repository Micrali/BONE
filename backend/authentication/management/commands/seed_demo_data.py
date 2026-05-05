from django.core.management.base import BaseCommand
from django.conf import settings

from authentication.models import Subject
from algorithms.bonevibauth.pipeline import BoneVibAuthPipeline
from algorithms.bonevibauth.signal_processing import generate_chirp

import numpy as np


class Command(BaseCommand):
    help = 'Seed demo BoneVibAuth subjects and templates'

    def handle(self, *args, **options):
        pipeline = BoneVibAuthPipeline(settings.BONEVIBAUTH)
        probe = generate_chirp()

        for user in range(3):
            external_id = f'demo-{user:02d}'
            Subject.objects.get_or_create(external_id=external_id, defaults={
                'display_name': f'演示用户{user + 1}',
                'device_model': 'Simulated BCE Device',
            })
            features = []
            for index in range(10):
                rng = np.random.default_rng(user * 100 + index)
                response = 0.78 * probe + 0.22 * np.roll(probe, index % 13)
                response = response + rng.normal(0, 0.035, len(probe))
                features.append(pipeline.extract_feature(response))
            pipeline.save_template(external_id, pipeline.build_template(features))

        self.stdout.write(self.style.SUCCESS('Demo data seeded successfully.'))
