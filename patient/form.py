from django import forms
from .models import PatientProfile
#DataFlair
class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields =['name','about','image']




