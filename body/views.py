import json
from datetime import datetime
from django.shortcuts import render
from .models import Person, Review
from rest_framework.generics import *
from .serializers import PersonSerializer, ReviewSerializer

# Create your views here.

# is ajax global function
def is_ajax(request):
    return request.headers.get('x-requested-with') == 'XMLHttpRequest'

# welcome view
def welcomePage(request):
    return render(request, "welcomePage.html")

# home page function view
def homePage(request):
    return render(request, "body/home.html")

# Person APIs
# list bodies API
class PersonListAPI(ListAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()
# add body API
class AddPersonAPI(CreateAPIView):
    serializer_class = PersonSerializer
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
# view body APi
class ViewPersonAPI(RetrieveAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()


# Review APIs
# list reviews API
class ReviewListAPI(ListAPIView):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

# add review API
class AddReviewAPI(CreateAPIView):
    pass