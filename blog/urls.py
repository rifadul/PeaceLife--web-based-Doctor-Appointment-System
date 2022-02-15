from django.urls import path
from .views import *

urlpatterns = [
    path('', blogView, name='blog'),
    path('<str:slug>/', blogDetailsView, name='blog_details'),
    path('categories/<int:id>/', filterByCategory, name='categories'),
    path('add_blog/', filterByCategory, name='add_blog'),
]
