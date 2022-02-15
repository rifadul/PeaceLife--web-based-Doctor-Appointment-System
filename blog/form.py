from django import forms
from .models import BlogPost
from django.utils.translation import gettext, gettext_lazy as _



class AddBlogPostForm(forms.Form):
    title = forms.CharField(
        label=_("Full Name"),
        required=True,
        widget= forms.TextInput(attrs={'class': 'form-control','placeholder': 'Full Name'})
    )
    content = forms.CharField(
        label=_("Your Post..."),
        required=True,
        widget= forms.Textarea(attrs={'class': 'form-control','placeholder': 'about'})
    )
    category = forms.ModelChoiceField(
        queryset = BlogPost.objects.all(),
        label=_("category"),
        required=True,
        widget= forms.Select(attrs={'class': 'form-control','placeholder': 'Department'})
    )
    image = forms.ImageField(
        label=_("Blog Image"),
    )
    class Meta:
        model = BlogPost
        fields =['title', 'content','category','image']