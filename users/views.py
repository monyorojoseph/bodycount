import requests
from django.shortcuts import redirect, render, get_object_or_404
from .models import Profile
from .forms import ProfileForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.conf import settings
from django.contrib import messages

# Create your views here.

# account creation
def registration(request):
    if request.user.is_authenticated:
        return redirect('body:home')

    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:signin')
    context = {"form": form}    
    return render(request, 'users/signup.html', context)

# signin
def signin(request):
    if request.user.is_authenticated:
        return redirect('body:home')

    if request.method == "POST":
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            "secret": settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            "response": recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        if result['success']:
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            
            request.session['password'] = "test123"

            if user is not None:
                login(request, user)
                return redirect("body:home")
        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
    return render(request, 'users/signin.html')

# signout
def signout(request):
    logout(request)
    return render(request, 'users/signout.html')

def close_account(request):
    pass

# profile, view and edit
@login_required
def edit_profile(request):
    user = request.user
    profile = get_object_or_404(Profile, user=user)
    if request.method == "POST":
        profile.email = request.POST['email']
        profile.username = request.POST['username']
        profile.age = request.POST['age']
        profile.sex = request.POST['sex']
        profile.sexuality = request.POST['sexuality']
        profile.favourite_porn = request.POST['favourite_porn']
        profile.target = request.POST['target']
        profile.save()

        return redirect('users:profile')
    return HttpResponse("Invalid request")
 

@login_required
def view_profile(request):
    profile_details = Profile.objects.get(user=request.user)
    context = {"profile_details": profile_details}
    return render(request, 'users/profile.html', context) 