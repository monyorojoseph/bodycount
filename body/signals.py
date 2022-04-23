from django.db.models.signals import pre_save, post_save
from .models import Person
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

# resize photo to (85,85)

# def pre_resize_photo(sender, instance, **kwargs):
#     with Image.open(instance.photo) as img:
#         if img.height > 100 or img.width > 100:
#             img.resize((85, 85))

# pre_save.connect(pre_resize_photo, sender=Person)

def post_resize_photo(sender, created, instance, **kwargs):
    if created:
        with Image.open(instance.photo) as img:
            if img.height > 100 or img.width > 100:
                img.thumbnail((85, 85))
                img = img.convert("RGB")
                output = BytesIO()
                img.save(output, format="JPEG")

                output.seek(0)
                instance.photo = InMemoryUploadedFile(output, 'ImageField',
                                          f'{instance.photo.name.split(".")[0]}.jpg',
                                          'image/jpeg', sys.getsizeof(output),
                                          None)

post_save.connect(post_resize_photo, sender=Person)