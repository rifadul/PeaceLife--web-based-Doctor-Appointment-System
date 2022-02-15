from django.db import models
from account.models import User
from doctor.models import Doctor
from .utils import Appointment_slug_generate
from ckeditor.fields import RichTextField
import datetime
# Create your models here.



class PaymentDetails(models.Model):
    payment_person= models.CharField(max_length=500,default='')
    transaction_id = models.CharField(max_length=500)
    amount = models.FloatField(max_length=100)
    card_type = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)
    transaction_date = models.CharField(max_length=100)
    risk_title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.transaction_id

GENDER_CHOICES = {
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
}

CONFIRMATION_STATUS = {
    ('Pending', 'Pending'),
    ('Accept', 'Accept'),
    ('Reject', 'Reject'),
}

APPOINTMENT_TYPE={
    ('Online','Online'),
    ('Offline','Offline'),
}


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    payment = models.ForeignKey(PaymentDetails, on_delete=models.CASCADE,null=True)
    appointment_id = models.CharField(max_length=200,null=True)
    patient_name = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=300, null=True, blank=True)
    gender = models.CharField(
        max_length=100, choices=GENDER_CHOICES, default='Male')
    age = models.IntegerField()
    mobile = models.CharField(max_length=12)
    email = models.EmailField(max_length=50)
    problem_brief = RichTextField()
    appointment_time = models.TimeField(auto_now=False,null=True)
    appointment_date = models.DateField(auto_now=False, null=True)
    appointment_type = models.CharField(
        max_length=100, choices=APPOINTMENT_TYPE, default='Online')
    confirmation_status = models.CharField(
        max_length=100, choices=CONFIRMATION_STATUS, default='Pending')
    pay_status = models.BooleanField(default=False, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patient_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = Appointment_slug_generate(self.patient_name)
        super(Appointment, self).save(*args, **kwargs)


