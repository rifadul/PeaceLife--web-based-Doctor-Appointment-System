from django.contrib import admin
from .models import Category,BlogPost
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('title',)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    '''Admin View for BlogPost'''

    list_display = ('title','category')

