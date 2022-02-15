from django.urls import path
from .views import *

urlpatterns = [
    path('patient_profile/', patientProfileView, name='patient_profile'),
    path('patient_profile_update/', patientProfileUpdateview, name='patient_profile_update'),
]
