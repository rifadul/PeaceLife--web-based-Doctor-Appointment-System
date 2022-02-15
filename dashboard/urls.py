from django.urls import path
from .views import *

urlpatterns = [
    path('', profileView, name='profile'),
    path('profile-update', profileUpdateView, name='profile-update'),
    # path('', doctorsView, name='doctors'),
    # path('<slug:slug>', doctorDetailsView, name='doctor_details'),
    # path('department/<int:id>', filterByDepartment, name='department'),
    # path('doctor_profile/', DoctorProfileView, name='doctor_profile'),
    # path('doctor_profile_update/', doctorProfileUpdateview, name='doctor_profile_update'),
    # path('doctor_schedule/', DoctorScheduleView, name='doctor_schedule'),
]
