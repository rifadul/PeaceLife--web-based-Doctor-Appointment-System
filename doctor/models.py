from django.db import models
from account.models import User
from .utils import department_slug_generate, doctor_slug_generate
from ckeditor.fields import RichTextField
# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='medical/department/')
    about = RichTextField()
    slug = models.SlugField(max_length=300, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = department_slug_generate(self.name)
        super(Department, self).save(*args, **kwargs)


DAY_CHOICES = {
    ('Saturday', 'Saturday'),
    ('Sunday', 'Sunday'),
    ('Monday', 'Monday'),
    ('Tuesday', 'Tuesday'),
    ('Wednesday', 'Wednesday'),
    ('Thursday', 'Thursday'),
    ('Friday ', 'Friday '),
}


class Doctor(models.Model):
    doctor = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=1000)
    slug = models.SlugField(max_length=300, null=True, blank=True)
    department = models.OneToOneField(Department, on_delete=models.CASCADE)
    designation = models.CharField(max_length=100)
    about = RichTextField()
    education = RichTextField()
    experience = RichTextField()
    consulting_fee = models.FloatField(null=True)
    image = models.ImageField(
        upload_to='Doctor/images/')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = doctor_slug_generate(self.full_name)
        super(Doctor, self).save(*args, **kwargs)


class DoctorSchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day = models.CharField(
        max_length=100, choices=DAY_CHOICES, default='Saturday')
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.day
