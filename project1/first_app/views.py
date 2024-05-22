from django.shortcuts import render
from django.http import HttpResponse
def courses(request):
    return HttpResponse("This is courses page")
def about(request):
    return HttpResponse("this is about pages")
# Create your views here.
