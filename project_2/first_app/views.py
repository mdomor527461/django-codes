from django.shortcuts import render
def home(request):
    return render(request,'first_app/home.html')
# Create your views here.
