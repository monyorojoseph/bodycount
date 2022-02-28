from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Review)
admin.site.register(Person)
admin.site.register(Reply)
# admin.site.register(Votes)