from django.shortcuts import render
def home(request):
    d = {'author' : 'rahim','age' : 6 ,  'lst': [1,2,3]}
    return render(request,'home.html',d)

# Create your views here.
