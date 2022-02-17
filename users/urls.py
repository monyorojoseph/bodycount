from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),
] 