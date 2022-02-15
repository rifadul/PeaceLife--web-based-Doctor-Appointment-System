from django import forms
from .models import Appointment
from django.forms.widgets import NumberInput, RadioSelect, TextInput
from django.utils.translation import gettext, gettext_lazy as _
# DataFlair


class AppointmentForm(forms.ModelForm):
    GENDER_CHOICES = {
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
    }
    APPOINTMENT_TYPE={
    ('Online','Online'),
    ('Offline','Offline'),
    }

    patient_name = forms.CharField(
        label=_("Patient Name"),
        required=True,
        widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Patient Full Name'})
    )
    gender  = forms.ChoiceField(
        label=_("Gender"),
        choices=GENDER_CHOICES,
        required=True,
        initial='Male',
        widget= forms.Select(attrs={'class': 'form-select'})
    )
    # mobile = forms.CharField(
    #     label=_("Phone Number"),
    #     required=True,
    #     widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Contact Namber'})
    # )
    age = forms.IntegerField(
        label=_("Patient Age"),
        required=True,
        widget= forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Age'})
    )
    
    # email = forms.EmailField(
    #     label=_("Email"),
    #     required=True,
    #     widget= forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'})
    # )
    problem_brief = forms.CharField(label=_("Problem Brief"),widget=forms.Textarea(attrs={'class': 'form-control','rows':5,'placeholder': 'Your Problem'}))

    appointment_type  = forms.ChoiceField(
        label=_("Appointment Type"),
        choices=APPOINTMENT_TYPE,
        initial='Online',
        widget= forms.Select(attrs={'class': 'form-select'})
    )

    appointment_date =   forms.DateField(label=_("Appointment Date"),widget=NumberInput(attrs={'class': 'form-control','type': 'date'}))
    class Meta:
        model = Appointment
        fields = ['patient_name','age', 'gender', 'appointment_type', 'appointment_date','problem_brief',]


class ConfirmationStatusForm(forms.ModelForm):
    CONFIRMATION_STATUS = {
        ('Pending', 'Pending'),
        ('Accept', 'Accept'),
        ('Reject', 'Reject'),
    }
    confirmation_status  = forms.ChoiceField(
        label=_("Confirmation"),
        choices=CONFIRMATION_STATUS,
        required=False,
        initial='Male',
        widget= forms.Select(attrs={'class': 'form-select'})
    )
    appointment_time = forms.TimeField(
        label=_("Appointment Time"),
        required=False,
        widget= forms.TimeInput(attrs={'class': 'form-control','placeholder': '09.30 pm','type': 'time'})
    )
    appointment_date =   forms.CharField(label=_("Appointment Date"),widget=TextInput(attrs={'class': 'form-control','type': 'date'}))
    class Meta:
        model = Appointment
        fields = ['confirmation_status','appointment_time', 'appointment_date']
