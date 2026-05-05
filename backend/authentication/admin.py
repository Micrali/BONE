from django.contrib import admin
from .models import AuthSession, HCRSample, Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('external_id', 'display_name', 'device_model', 'created_at')
    search_fields = ('external_id', 'display_name', 'device_model')


@admin.register(HCRSample)
class HCRSampleAdmin(admin.ModelAdmin):
    list_display = ('subject', 'purpose', 'sample_rate', 'duration_seconds', 'created_at')
    list_filter = ('purpose', 'sample_rate')
    search_fields = ('subject__external_id',)


@admin.register(AuthSession)
class AuthSessionAdmin(admin.ModelAdmin):
    list_display = ('subject', 'score', 'threshold', 'accepted', 'latency_ms', 'created_at')
    list_filter = ('accepted',)
    search_fields = ('subject__external_id',)
