from django.urls import path
from .views import *

urlpatterns = [
    path('welcome', welcomePage, name="welcomePage"),
    path('home/', homePage, name='homePage'),
    path('all_bodies/', allBodies, name='allBodies'),
    path('add_body/', addBody, name='addBody'),
]