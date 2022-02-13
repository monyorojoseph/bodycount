from django.shortcuts import render, get_list_or_404
from django.http import JsonResponse, HttpResponse
from django.core import serializers
from django.views import View
from .models import Person, Review
from .forms import PersonForm, ReviewForm

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

# all bodies function view
def allBodies(request):
    if is_ajax and request.method == "GET":
        all_bodies = list(Person.objects.all())
        response = serializers.serialize('json', all_bodies)
        return HttpResponse(response, content_type='application/json', status=200)
    return JsonResponse({'error': 'Invalid request'}, status=400)

# add body function view
def addBody(request):
    if is_ajax and request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            instance = form.save()
            response = serializers.serialize('json', instance)

            return HttpResponse(response, status=200, content_type='application/json')
        return JsonResponse({'error': form.errors}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)



# create, list and view review class view
class ReviewClassVIew(View):
    model = Review

    # get review lists method

    # add review method

    # view review method