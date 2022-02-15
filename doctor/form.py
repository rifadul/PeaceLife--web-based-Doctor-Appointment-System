from django import forms
from .models import Doctor, DoctorSchedule,Department
from django.utils.translation import gettext, gettext_lazy as _
# DataFlair

class DoctorProfileForm(forms.ModelForm):
    full_name = forms.CharField(
        label=_("Full Name"),
        required=True,
        widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Full Name'})
    )
    department = forms.ModelChoiceField(
        queryset = Department.objects.all(),
        label=_("Department"),
        required=True,
        widget= forms.Select(attrs={'class': 'form-control','placeholder': 'Department'})
    )
    designation = forms.CharField(
        label=_("Designation"),
        required=True,
        widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Designation'})
    )
    about = forms.CharField(
        label=_("About"),
        required=True,
        widget= forms.Textarea(attrs={'class': 'form-control','placeholder': 'about'})
    )
    education = forms.CharField(
        label=_("Education"),
        required=True,
        widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Education'})
    )
    experience = forms.CharField(
        label=_("Experience"),
        required=True,
        widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Experience'})
    )
    consulting_fee = forms.IntegerField(
        label=_("Consulting Fee"),
        required=True,
        widget= forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Consulting Fee'})
    )
    image = forms.ImageField(
        label=_("Profile Image"),
    )
    
    class Meta:
        model = Doctor
        fields = ['full_name', 'department', 'designation',
                  'about', 'education', 'experience','consulting_fee', 'image']


class DoctorScheduleForm(forms.ModelForm):
    DAY_CHOICES = {
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday ', 'Friday '),
}
    day = forms.ChoiceField(
        label=_("Day"),
        choices=DAY_CHOICES,
        initial='Saturday',
        widget= forms.Select(attrs={'class': 'form-select'})
    )
    start_time = forms.TimeField(
        label=_("Start Time"),
        required=True,
        widget= forms.TimeInput(attrs={'class': 'form-control','type': 'time'})
    )

    end_time = forms.TimeField(
        label=_("End Time"),
        required=True,
        widget= forms.TimeInput(attrs={'class': 'form-control','type': 'time'})
    )
    class Meta:
        model = DoctorSchedule
        fields = ['day', 'start_time', 'end_time']
