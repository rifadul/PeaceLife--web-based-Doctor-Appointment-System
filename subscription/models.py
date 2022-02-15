from django.db import models
from colorfield.fields import ColorField
from appointment.models import PaymentDetails
from account.models import User

# Create your models here.

class PlanFeature(models.Model):
    feature_name = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.feature_name


class PricePlan(models.Model):
    plan_name = models.CharField(max_length=255)
    heading_color = ColorField(default='#07d5c0')
    plan_price = models.FloatField()
    plan_image = models.ImageField(upload_to="Subscription/",null=True)
    features = models.ManyToManyField(PlanFeature)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plan_name


class Subscription(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=255)
    subscription_id = models.CharField(max_length=200,null=True)
    plan_price = models.FloatField()
    payment = models.ForeignKey(PaymentDetails, on_delete=models.CASCADE,null=True)
    subscribe = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)






