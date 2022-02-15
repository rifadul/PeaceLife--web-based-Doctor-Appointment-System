from django.urls import path
from .views import *

urlpatterns = [
    path('', subscriptionPackageView, name='subscription'),
    path('buy-package', subscriptionView, name='buyPackage'),
    path('status/<str:subscription>/<str:trans_id>/', subscription_payment_status,name='package_payment_status')
]
