import json
from django.shortcuts import redirect, render
from users.forms import ProfileForm
from .models import Profile
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.contrib import messages
from django.core import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.

"""
    Check username and email if it's unique before registration
"""
def check_mail(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if request.method == 'POST' and is_ajax:
        email = json.load(request).get("email")
        if  User.objects.filter(email=email).exists():
            return JsonResponse({"valid": True}, status=200)
        else:
            return JsonResponse({"valid": False}, status=200)
    
    return JsonResponse({"message": "Invalid request"}, status=400)

def check_username(request):
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if request.method == 'POST' and is_ajax:
        username = json.load(request).get("username")
        if  User.objects.filter(username=username).exists():
            return JsonResponse({"valid": True}, status=200)
        else:
            return JsonResponse({"valid": False}, status=200)
    
    return JsonResponse({"message": "Invalid request"}, status=400)



"""
    Authentication view: registration, sign in, sign out, closing account

"""

# sign in
def signin(request):
    if request.user.is_authenticated:
        return redirect('body:home')
    
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if request.method == 'POST' and is_ajax:
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            # if request.session.test_cookie_worked():
            #     request.session.set_expiry(31536000)
        else:
            return JsonResponse({"message":"Invalid credentials"}, status=400)

    # request.session.set_test_cookie()
    return render(request, 'users/signin.html')

# signout
@login_required
def signout(request):
    logout(request)
    return render(request, 'users/signout.html')

# account removal
@login_required
def close_account(request):
    user = User.objects.get(email=request.user.email)
    logout(request)
    user.delete()
    return render(request, 'users/close_account.html')


"""
    profile view: view profile, edit profile

"""

# edit profile details
@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if request.method == 'POST' and is_ajax:
        profile.user = request.user
        profile.email = request.POST['email']
        profile.username = request.POST['username']
        profile.age = request.POST['age']
        profile.gender = request.POST['gender']
        profile.save()
        return JsonResponse({"succes":"yaay ..."}, status=200)

    return JsonResponse({"error": "Invalid request method"}, status=400)
 
# view profile details
@login_required
def view_profile(request):
    profile = Profile.objects.get(user = request.user)
    form = ProfileForm(instance=profile)
    is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'

    if request.method == 'GET' and is_ajax:
        profile = Profile.objects.get(user=request.user)
        serialized_profile = serializers.serialize('json', [profile,])
        return JsonResponse({"profile": serialized_profile}, status=200, safe=False)
        
    return render(request, 'users/profile.html', {"form":form}) 