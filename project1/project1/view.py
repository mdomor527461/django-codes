from django.http import HttpResponse
def contact(request):
    return HttpResponse("hello world this is contact page")
def home(reques):
    return HttpResponse("this is home page")