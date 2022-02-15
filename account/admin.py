from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import urls
# Register your models here.

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     '''Admin View for User'''

#     list_display = ('username','email','first_name','last_name','phone','user_type','is_staff', 'is_active',)


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username','email','first_name','last_name','phone','user_type','is_staff', 'is_active',)
    list_filter = ('username','email','first_name','last_name','user_type', 'is_staff', 'is_active',)
    fieldsets = (
        ("Account info", {'fields': ('username','email', 'user_type', 'password')}),
        ("Personal info", {'fields': ('first_name','last_name', 'phone')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser','groups','user_permissions')}),   #'is_customer' , 'is_seller'
        ('Important dates', {'fields': ('last_login',)}),   #'is_customer' , 'is_seller'
    )
    add_fieldsets = (
        ('Account info', {
            'classes': ('wide',),
            'fields': ('username', 'email', 'user_type', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
        ('User Info', {
            'classes': ('wide',),
            'fields': ('first_name','last_name','phone','profile_image',)}
        ),
    )
    search_fields = ('email','first_name','last_name','user_type')
    ordering = ('email',)