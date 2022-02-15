from django.db import models
from account.models import User
from .utils import blogPost_slug_generate,category_slug_generate
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField #import this
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=300, null=True,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = category_slug_generate(self.title)
        super(Category, self).save(*args, **kwargs) 


class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    content = RichTextUploadingField()
    slug = models.SlugField(max_length=300, null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='Blog_images/')
    publish = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = blogPost_slug_generate(self.title)
        super(BlogPost, self).save(*args, **kwargs) 



# class Comment(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
#     content = RichTextField()
#     create_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return self.user.first_name