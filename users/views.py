from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Profile
from .forms import ProfileForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

# account creation
def registration(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('body:home')
    context = {
        "form": form
    }    
    return render(request, 'users/signup.html', context)

# signin
def signin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('body:home')

    return render(request, 'users/signin.html')

# signout
def signout(request):
    logout(request)
    return render(request, 'users/signout.html')

def close_account(request):
    pass

# creation of profile, view and edit
def create_profile(request):
    pass

def edit_profile(request):
    pass

def view_profile(request):
    pass