from django.urls import path
from .views import *

app_name = "body"

urlpatterns = [
    path('', welcome, name="welcome"),
    path('home/', home, name='home'),
    path('add_person/', add_person, name='add_person'),
    path('reviews/', reviews, name='reviews'),
    path('add_review/', add_review, name='add_review')
]