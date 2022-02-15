from django.contrib import admin
from .models import Appointment,PaymentDetails
# Register your models here.


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient_name','doctor','problem_brief','payment','pay_status')

    
@admin.register(PaymentDetails)
class PaymentDetailsAdmin(admin.ModelAdmin):
    '''Admin View for PaymentDetails'''

    list_display = ('payment_person','transaction_id','amount','card_type','payment_status')


