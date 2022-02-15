from django.urls import path
from .views import *

urlpatterns = [
    path('', appointmentView, name='appointment'),
    # path('appointment_list', appointmentListView, name='appointment_list'),
    # path('<slug:slug>', appointmentDetailsView, name='appointment_details'),
    path('appointment-confirmation/<slug:slug>', appointmentConfirmation, name='confirmation'),
    path('appointment-list', appointmentListView, name='appointment-list'),
    path('status/<str:appointment>/<str:pay>/', payment_status,name='payment_status')
]
    