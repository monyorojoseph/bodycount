from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.conf import settings
from django.contrib.auth.models import PermissionsMixin

User = settings.AUTH_USER_MODEL

# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True
    

    def create_user(self, email, password, **extra_fields ):
        
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email = self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)



    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = "user"
    
    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avators', null=True, blank=True)
    username = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=200, null=True, blank=True)
    personal_name = models.CharField(max_length=200, null=True, blank=True)
    age = models.CharField(max_length=8, null=True, blank=True)
    sexuality = models.CharField(max_length=200, null=True, blank=True)
    sex = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    bodycount_target = models.CharField(max_length=200, null=True, blank=True)
    favorite_porn = models.CharField(max_length=200, null=True, blank=True)
    fetish = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.username