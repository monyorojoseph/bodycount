from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Person, Review
from .forms import PersonForm, ReviewForm
from users.forms import UserCreationForm
from django.contrib.auth import authenticate, login


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
        password = request.POST['password1']

        if request.session.test_cookie_worked():
            request.session['email'] = email

        if form.is_valid():
            form.save()
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({"message":"User created successfully"}, status = 200)
        # else return form errors in json response
    context = {"form": form} 

    request.session.set_test_cookie()
   
    return render(request, 'welcome.html', context)

"""
    Home page displays all bodies that have been added
"""
    
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
    
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if request.method == 'POST' and is_ajax:
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
            return JsonResponse({
                "message": "Person added successfully"
            }, status=200)
        return JsonResponse({"message":"Invalid form data"}, status=400)
    return JsonResponse({"message":"Invalid request"}, status=400)


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
        return JsonResponse({"message":"Invalid form data"}, status=400)
    return JsonResponse({"message":"Invalid request"}, status=400)