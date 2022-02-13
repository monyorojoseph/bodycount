from distutils.command.upload import upload
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.
class Person(models.Model):
    full_name = models.CharField(max_length=200)
    photo = models.ImageField(null=True, blank=True, upload_to='photos')
    phone = models.CharField(max_length=200, null=True, blank=True)
    age = models.CharField(max_length=5, null=True, blank=True)
    sex = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    rating = models.CharField(max_length=200, null=True, blank=True)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=False)

    class Meta:
        ordering = ['-date_added']
    
    def __str__(self):
        return str(self.full_name)



class Review(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    comments = models.TextField()

    def __str__(self):
        return str(self.user)
    