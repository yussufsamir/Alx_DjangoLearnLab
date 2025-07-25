from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager
from django.contrib.auth.models import Permission

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year  = models.IntegerField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

 
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)

    class Meta:
        permissions = [
            ('can_view', 'Can view article'),
            ('can_create', 'Can create article'),
            ('can_edit', 'Can edit article'),
            ('can_delete', 'Can delete article'),
        ]


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    objects = CustomUserManager()

    def __str__(self):
        return self.username    

     
  