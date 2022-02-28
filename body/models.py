from django.utils import timezone
from django.db import models
from django.conf import settings
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django_cryptography.fields import encrypt


User = settings.AUTH_USER_MODEL


# Create your models here.
class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bodies')
    full_name = encrypt(models.CharField(max_length=200))
    photo = encrypt(models.ImageField(null=True, blank=True, upload_to='photos'))
    phone = encrypt(models.CharField(max_length=200, null=True, blank=True))
    age = encrypt(models.CharField(max_length=5, null=True, blank=True))
    location = models.CharField(max_length=200, null=True, blank=True)
    rating = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField(default=timezone.now())

    class Meta:
        ordering = ['-id']
        verbose_name = 'Person'

    
    def __str__(self):
        return str(self.full_name)

    def save(self, *args, **kwargs):
        # Opening the uploaded image
        img = Image.open(self.photo)

        if img.height > 200 or img.width > 200:

            output_size = (200, 200)
            img.thumbnail(output_size)
            img = img.convert('RGB')

            output = BytesIO()
            img.save(output, format='JPEG')
            output.seek(0)

            # change the photofield value to be the newley modifed photo value
            self.photo = InMemoryUploadedFile(output, 'photoField',
                                            f'{self.photo.name.split(".")[0]}.jpg',
                                            'image/jpeg', sys.getsizeof(output),
                                            None)

        super().save(*args, **kwargs)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    review_text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now())


    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Review'


    def __str__(self):
        return str(self.user.username)    

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    repy_text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now())


    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Reply'

    def __str__(self):
        return str(self.user.username)  


# class Votes(models.Model):
#     vote_title = models.CharField(max_length=200)
#     count = models.PositiveIntegerField(default=0)

#     class Meta:
#         verbose_name = 'Votes'

#     def __str__(self):
#         return self.vote_title  