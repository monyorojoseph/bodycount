from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Person, Review
from .forms import PersonForm, ReviewForm
from users.forms import UserCreationForm

# home view
def welcome(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:signin')
    context = {"form": form}    
    return render(request, 'welcome.html', context)
    
@login_required
def home(request):
    form = PersonForm()
    persons_list = Person.objects.filter(user=request.user)
    context = {
        "form": form,
        "persons_list":persons_list
    }
    return render(request, 'body/home.html', context)

# add body
@login_required
def add_person(request):
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            print(request.POST)
            user = request.user
            Person.objects.create(
                user=user,
                full_name=request.POST['full_name'],
                photo=request.FILES['photo'],                
                phone=request.POST['phone'],                
                age=request.POST['age'],                
                location=request.POST['location'],                
                rating=request.POST['rating']
            )
            return redirect('body:home')
        return HttpResponse("Invalid form data")
    return HttpResponse("Invalid request")


# view body details
@login_required
def view_person(request):
    context = {}
    return render(request, 'body/home.html', context)


# review views
def reviews(request):
    review_list = Review.objects.all()
    total_reviews = Review.objects.all().count()
    form = ReviewForm()
    context = {
        "review_list": review_list,
        "form": form,
        "total_reviews": total_reviews
    }
    return render(request, 'body/reviews.html', context)

@login_required
def add_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        print(request.POST, form.is_valid())
        if form.is_valid():
            Review.objects.create(user=request.user, comments=request.POST['comments'])
            return redirect('body:reviews')
        return HttpResponse("Invalid form data")
    return HttpResponse("Invalid request")