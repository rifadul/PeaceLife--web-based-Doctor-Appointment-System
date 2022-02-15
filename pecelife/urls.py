from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('team', teamMembersView, name='teamMember'),
    # path('contact', contactView, name='contact'),
    path('contact', contactView, name='contact'),
]
