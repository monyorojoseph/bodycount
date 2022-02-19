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
        verbose_name = 'Person'

    
    def __str__(self):
        return str(self.full_name)
    
    def photo_url(self):
        return self.photo.url

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    review_text = models.TextField()

    class Meta:
        ordering = ['-id']
        verbose_name = 'Review'


    def __str__(self):
        return str(self.user.username)    

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    repy_text = models.TextField()

    class Meta:
        ordering = ['-id']
        verbose_name = 'Reply'

    def __str__(self):
        return str(self.user.username)  


class Votes(models.Model):
    vote_title = models.CharField(max_length=200)
    count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = 'Votes'

    def __str__(self):
        return self.vote_title  