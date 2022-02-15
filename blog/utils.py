import random
import string
from django.utils.text import slugify
   

def generate_random_string(N):
    res = ''.join(random.choices(string.ascii_lowercase +
                             string.digits, k = N))
    return res


def blogPost_slug_generate(text):
    from .models import BlogPost
    new_slug = slugify(text)
    if BlogPost.objects.filter(slug=new_slug).first():
        return blogPost_slug_generate(text+generate_random_string(5))
    return new_slug

def category_slug_generate(text):
    from .models import Category
    new_slug = slugify(text)
    if Category.objects.filter(slug=new_slug).first():
        return blogPost_slug_generate(text+generate_random_string(5))
    return new_slug
