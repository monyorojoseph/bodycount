from django.urls import path
from .views import *

urlpatterns = [
    path('welcome', welcomePage, name="welcomePage"),
    path('home/', homePage, name='homePage'),
    path('personlistapi/', PersonListAPI.as_view(), name='allBodies'),
    path('createpersonapi/', AddPersonAPI.as_view(), name='addBody'),
    path('reviewlistapi/', ReviewListAPI.as_view(), name='allReviews'),
    path('createreviewapi/', AddReviewAPI.as_view(), name='addReview'),
]