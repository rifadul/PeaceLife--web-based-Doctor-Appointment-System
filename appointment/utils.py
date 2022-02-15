import random
import string
from django.utils.text import slugify
   

def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k = N))
    return res



def Appointment_slug_generate(text):
    from .models import Appointment
    new_slug = slugify(text)
    if Appointment.objects.filter(slug=new_slug).first():
        return Appointment_slug_generate(text+generate_random_string(5))
    return new_slug
