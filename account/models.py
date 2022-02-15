from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
from .managers import CustomUserManager

# Create your models here.

class LowercaseEmailField(models.EmailField):
    """
    Override EmailField to convert emails to lowercase before saving.
    """
    def to_python(self, value):
        """
        Convert email to lowercase.
        """
        value = super(LowercaseEmailField, self).to_python(value)
        # Value can be None so check that it's a string before lowercasing.
        if isinstance(value, str):
            return value.lower()
        return value


class User(AbstractBaseUser,PermissionsMixin):
    userType = (
        ('Patient','Patient'),
        ('Doctor','Doctor'),
    )

    email = LowercaseEmailField(_('email address'), unique=True)
    username = models.CharField(_('username'), max_length=150,unique=True)
    first_name = models.CharField(max_length=255, blank = True)
    last_name = models.CharField(max_length=255, blank = True)
    # if you require phone number field in your project
    phone_regex = RegexValidator( regex = r'^\d{11}$',message = "phone number should exactly be in 11 digits")
    phone = models.CharField(max_length=255, validators=[phone_regex], blank = True, null=True)  # you can set it unique = True
    profile_image = models.ImageField(upload_to='user_profile_pic',default='user_profile_pic/avatar.png')
    user_type = models.CharField(max_length=255,choices=userType)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone']

    class Meta:
        verbose_name = "Accounts"
        verbose_name_plural ="Accounts"
    
    def __str__(self):
        return self.username
    
    def full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    
