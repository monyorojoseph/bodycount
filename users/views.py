import requests
from django.shortcuts import redirect, render
from .models import Profile
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.contrib import messages

# Create your views here.

"""
    Authentication view: registration, sign in, sign out, closing account

"""

# registration
# def registration(request):
#     if request.user.is_authenticated:
#         return redirect('body:home')

#     form = UserCreationForm()
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)        
#         email = request.POST['email']
#         password = request.POST['password1']

#         if form.is_valid():
#             form.save()
#             user = authenticate(email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return JsonResponse({"message":"User created successfully"}, status=200)
#         return JsonResponse({"message":"Invalid from"}, status = 400)  # modify later to return form errors
#     context = {"form": form}    
#     return render(request, 'users/signup.html', context)

# sign in
def signin(request):
    if request.user.is_authenticated:
        return redirect('body:home')
    
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if request.method == 'POST' and is_ajax:

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
            
            if user is not None:
                login(request, user)
                if request.session.test_cookie_worked():
                    request.session.set_expiry(31536000)


        else:
            return JsonResponse({"message":"Invalid reCAPTCHA. Please try again."}, status = 400)
    request.session.set_test_cookie()
    return render(request, 'users/signin.html')

# signout
def signout(request):
    logout(request)
    return render(request, 'users/signout.html')

# account removal
def close_account(request):
    pass

"""
    profile view: view profile, edit profile

"""

# edit profile details
@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

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
 
# view profile details
@login_required
def view_profile(request):
    profile_details = Profile.objects.get(user=request.user)
    context = {"profile_details": profile_details}
    return render(request, 'users/profile.html', context) 