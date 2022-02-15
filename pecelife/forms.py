from django import forms
from .models import Contact
from django.utils.translation import gettext, gettext_lazy as _
# DataFlair


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        label=_("Name"),
        widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'})
    )
    email = forms.EmailField(
        label=_("Email"),
        required=True,
        widget= forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'})
    )
    subject = forms.CharField(
        label=_("Subject"),
        widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Subject'})
    )
    phone = forms.CharField(
        label=_("Phone Number"),
        widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Your Phone Number'})
    )
    message = forms.CharField(
        label=_("Message"),
        widget= forms.Textarea(attrs={'class': 'form-control','placeholder': 'Message'})
    )
    class Meta:
        model = Contact
        fields = '__all__'