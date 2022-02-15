from django.urls import path
from .views import *

urlpatterns = [
    path('', doctorsView, name='doctors'),
    path('details/<slug:slug>', doctorDetailsView, name='doctor_details'),
    path('department/<int:id>', filterByDepartment, name='department'),
    path('doctor_profile', DoctorProfileView, name='doctor_profile'),
    path('doctor_profile_update/', doctorProfileUpdateview, name='doctor_profile_update'),
    path('add_schedule', DoctorScheduleView, name='add-schedule'),
]
