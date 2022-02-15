from django.urls import path
from .views import MessengerView
from django.contrib.auth.decorators import login_required

urlpatterns = [
     #path('', MessengerView.as_view(),name='messenger'),
    path('<str:username>/', MessengerView.as_view(),name='messenger'),
]