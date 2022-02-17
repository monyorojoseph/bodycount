from django.urls import path
from .views import *

app_name = "body"

urlpatterns = [
    path('', welcome, name="welcome"),
    path('home/', home, name='home'),
    path('add_person/', add_person, name='add_person'),
    path('reviews/', reviews, name='reviews'),
    path('add_review/', add_review, name='add_review'),
    # path('review/', reviewPage, name='reviewPage'),
    # path('personlistapi/', PersonListAPI.as_view(), name='allBodies'),
    # path('createpersonapi/', AddPersonAPI.as_view(), name='addBody'),
    # path('reviewlistapi/', ReviewListAPI.as_view(), name='allReviews'),
    # path('createreviewapi/', AddReviewAPI.as_view(), name='addReview'),
]