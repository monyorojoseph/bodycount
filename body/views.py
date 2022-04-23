import logging
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Person, Review
from .forms import PersonForm, ReviewForm
from users.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.core import serializers
from django.contrib.auth import get_user_model
from django.utils import timezone

logger = logging.getLogger(__name__)

User = get_user_model()

"""
    Landing page also has sign up form
"""
# home view
def welcome(request):

    if request.user.is_authenticated:
        return redirect('body:home')

    form = UserCreationForm()
    
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if request.method == 'POST' and is_ajax:
        form = UserCreationForm(request.POST)        
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password1']

        if form.is_valid():
            form.save()
            total_users = User.objects.all().count()
            logger.info(f"[ User {total_users}] email :- {email} username :- {username}")
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({"message":"User created successfully"}, status = 200)
        return JsonResponse({"message": "Invalid form"}, status=400)
        
    context = {"form": form} 

    # request.session.set_test_cookie()
   
    return render(request, 'welcome.html', context)

"""
    Home page displays all bodies that have been added
"""
    
@login_required
def home(request):  
    form = PersonForm()
        
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if request.method == 'GET' and is_ajax:
        persons_list = list(Person.objects.filter(user=request.user).values())
        return JsonResponse({"persons_list": persons_list}, status = 200)

    return render(request, 'body/home.html', {"form": form})

# add body
@login_required
def add_person(request):
    
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if request.method == 'POST' and is_ajax:
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            new_person = Person.objects.create(
                user=user,
                full_name=request.POST['full_name'],
                photo=request.FILES['photo'],                
                phone=request.POST['phone'],                
                age=request.POST['age'],                
                location=request.POST['location'], 
                rating = request.POST['rating']    
            )
            person = serializers.serialize("json", [new_person,])
            return JsonResponse({"person":  person}, status=200, safe=False)
        return JsonResponse({"message":"Invalid form data"}, status=400)
    return JsonResponse({"message":"Invalid request"}, status=400)


# review views
def reviews(request):
    form = ReviewForm()
        
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if request.method == 'GET' and is_ajax:        
        review_list = list(Review.objects.all().values())
        total_reviews = Review.objects.all().count()

        return JsonResponse({
            'review_list':review_list,
            "total_reviews":total_reviews
        }, status = 200)

    return render(request, 'body/reviews.html', {"form": form})

@login_required
def add_review(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if request.method == 'POST' and is_ajax: 
        form = ReviewForm(request.POST)
        if form.is_valid():                               
            new_review = Review.objects.create(user=request.user, review_text=request.POST['review_text'], username=request.user.username )
            review = serializers.serialize('json', [new_review,])
            return JsonResponse({"review":review}, status = 200)
        return JsonResponse({"message":"Invalid form data"}, status=400)
    return JsonResponse({"message":"Invalid request"}, status=400)

