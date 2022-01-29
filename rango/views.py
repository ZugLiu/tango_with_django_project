from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    response = HttpResponse("Rango says hey there partner!")
    response.write('<a href=\'/rango/about/\'>About</a>')
    return response

def about(request):
    response = HttpResponse("Rango says here is the about page." )
    response.write('<a href=\'/rango/\'>Index</a>')
    return response