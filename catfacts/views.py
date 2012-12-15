from django.http import HttpResponse
from django.shortcuts import render
from random import choice

from catfacts.models import Fact

# Home page view
def home(request):
    facts = Fact.objects.all()
    context = {'rand_fact': choice(facts)}
    return render(request, 'catfacts/home.html', context)

# FAQ page view
def faq(request):
#    return HttpResponse("This is my FAQ page!")
    return render(request, 'catfacts/temp.html')

# About page view
def about(request):
    return HttpResponse("This is my About page!")
