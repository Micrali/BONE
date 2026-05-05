from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health, name='health'),
    path('chirp-config/', views.chirp_config, name='chirp-config'),
    path('enroll/', views.enroll, name='enroll'),
    path('verify/', views.verify, name='verify'),
    path('metrics/', views.metrics, name='metrics'),
]
