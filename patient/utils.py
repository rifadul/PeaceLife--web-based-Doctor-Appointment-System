import random
import string
from django.utils.text import slugify
   

def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k = N))
    return res



def PatientProfile_slug_generate(text):
    from .models import PatientProfile
    new_slug = slugify(text)
    if PatientProfile.objects.filter(slug=new_slug).first():
        return PatientProfile_slug_generate(text+generate_random_string(5))
    return new_slug
