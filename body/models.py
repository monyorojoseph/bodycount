from django.utils import timezone
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.
class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bodies')
    full_name = models.CharField(max_length=200)
    photo = models.ImageField(null=True, blank=True, upload_to='photos')
    phone = models.CharField(max_length=200, null=True, blank=True)
    age = models.CharField(max_length=5, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    rating = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ['-id']
    
    def __str__(self):
        return str(self.full_name)
    
    def photo_url(self):
        return self.photo.url
    



class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    comments = models.TextField()

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.user)    