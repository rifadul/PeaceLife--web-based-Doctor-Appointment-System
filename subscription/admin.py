from django.contrib import admin
from .models import PricePlan,PlanFeature,Subscription

# Register your models here.

@admin.register(PlanFeature)
class PlanFeatureAdmin(admin.ModelAdmin):
    '''Admin View for PlanFeature'''
    
    list_display = ('feature_name',)


@admin.register(PricePlan)
class PricePlanAdmin(admin.ModelAdmin):
    '''Admin View for PricePlan'''

    list_display = ('plan_name','plan_price',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    '''Admin View for Subscription'''

    list_display = ('name','plan_name','plan_price',)

