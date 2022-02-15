from django.db import models
from account.models import User
from .utils import PatientProfile_slug_generate
from ckeditor.fields import RichTextField
# Create your models here.


class PatientProfile(models.Model):
    patient = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=300, null=True,blank=True)
    about = RichTextField()
    image = models.ImageField(upload_to='Doctor/images/')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = PatientProfile_slug_generate(self.name)
        super(PatientProfile, self).save(*args, **kwargs) 
