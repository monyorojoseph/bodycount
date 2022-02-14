from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *

# unregister models
admin.site.unregister(Group)

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Profile)