from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class TermsAndConditions(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=12)
    message = RichTextField()
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    content = models.TextField(max_length=255)
    image = models.ImageField(upload_to='testimonial_images/')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    about = models.TextField(max_length=255)
    image = models.ImageField(upload_to='team_member_images/')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Gallery(models.Model):
    gallery_image = models.ImageField(upload_to="Gallery_images/")
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class FrequentlyQuestion(models.Model):
    question = models.CharField(max_length=255)
    answer =  models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Service(models.Model):
    icon_class_name = models.CharField(max_length=255)
    service_name = models.CharField(max_length=255)
    about_service = models.CharField(max_length=255)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)