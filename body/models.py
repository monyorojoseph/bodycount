from django.db import models
from django.conf import settings
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys
from django.core.validators import MaxValueValidator, MinValueValidator



User = settings.AUTH_USER_MODEL


# Create your models here.
class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bodies')
    full_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos')
    phone = models.CharField(max_length=200)
    age = models.IntegerField(default=18)
    location = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0, validators=[
                                   MaxValueValidator(5),
                                   MinValueValidator(0) 
                                ])

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
            self.photo = InMemoryUploadedFile(output, 'ImageField',
                                            f'{self.photo.name.split(".")[0]}.jpg',
                                            'image/jpeg', sys.getsizeof(output),
                                            None)

        super().save(*args, **kwargs)

class Review(models.Model):
    user =  models.ForeignKey(User, models.SET_NULL, blank=True, null=True, related_name="user_reviews")
    username = models.CharField(max_length=200, null=True, blank=True)
    review_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-id']
        verbose_name = 'Review'


    def __str__(self):
        return str(self.user.username)    