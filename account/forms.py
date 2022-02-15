from django import forms
from .models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth import password_validation

class LoginForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        widget= forms.EmailInput(attrs={'class': 'input-box','placeholder': 'Email'})
    )

    password = forms.CharField(
        required=True,
        widget= forms.PasswordInput(attrs={'class': 'input-box','placeholder': 'Password'})
    )
    class Meta:
        model = User
        fields = ['email','password']

class SignupForm(UserCreationForm):
    USER_TYPE = {
    ('Patient', 'Patient'),
    ('Doctor', 'Doctor'),
    }
    first_name = forms.CharField(
        label=_("First Name"),
        required=True,
        widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        label=_("Last Name"),
        required=True,
        widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name'})
    )

    username = forms.CharField(
        label=_("Username"),
        required=True,
        widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Username'})
    )

    email = forms.EmailField(
        label=_("Email"),
        required=True,
        widget= forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'})
    )

    phone = forms.CharField(
        label=_("Phone Number"),
        required=True,
        widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Contact Number'})
    )
    

    password1 = forms.CharField(
        label=_("Password"),
        required=True,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'form-control','placeholder': 'Password'}),
    )
    password2 = forms.CharField(
        label=_("Password Confirmation"),
        required=True,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'form-control','placeholder': 'Confirm Password'}),
        help_text=_("Enter the same password as before, for verification."),
    )
    
    
    user_type  = forms.ChoiceField(
        label=_("Are You"),
        choices=USER_TYPE,
        required=True,
        widget= forms.RadioSelect()
    )
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','phone','password1', 'password2', 'user_type']


class AccountPasswordchangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label=_("Current Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True,'class': 'form-control','placeholder': 'Old password'}),
    )
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'form-control','placeholder': 'New password'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("Re-enter New Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class': 'form-control','placeholder': 'New confirmation password'}),
    )


class AccountPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label=_("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email','class': 'form-control'})
    )


class AccountsetPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New password"),strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'input-box','placeholder': 'Password'}),help_text=password_validation.password_validators_help_text_html())
    new_password2 = forms.CharField(label=_("Confirm New Password"),strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'input-box','placeholder': 'Confirm Password'})
)
