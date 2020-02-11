from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

from region.models import Region

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email_address'), unique=True)
    number = models.CharField(max_length=10, blank=False, help_text='contact_phone_number', unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True, related_name='user')
    USERNAME_FIELD = 'number'
    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.first_name

class Profile(models.Model):
    user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE, related_name='profile', unique=True)
    first_name = models.CharField(max_length=15, help_text='first_name')
    last_name = models.CharField(max_length=15, help_text='last_name')
    photo = models.ImageField(upload_to='images/user/', null=True, blank=True)
    balance = models.IntegerField(default=0)
    registration_date = models.DateTimeField(auto_now_add=True)

class Photo(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='images/user/', null=True, blank=True)

