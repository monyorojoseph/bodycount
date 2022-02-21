from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Person, Review
from .forms import PersonForm, ReviewForm
from users.forms import UserCreationForm

# home view
def welcome(request):

    if request.user.is_authenticated:
        return redirect('body:home')

    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('users:signin')
    context = {"form": form} 

    request.session.set_test_cookie()
   
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
        if form.is_valid():
            Review.objects.create(user=request.user, review_text=request.POST['review_text'])
            return redirect('body:reviews')
        return HttpResponse("Invalid form data")
    return HttpResponse("Invalid request")