from tabnanny import check
from django.shortcuts import render

# check username view

# check email view

# register view
def register_view(request):
    return render(request, 'accounts/signup.html')

# login view
def login_view(request):
    return render(request, 'accounts/signin.html')

# create, view, update profile class view

# change password view

# reset pasword view