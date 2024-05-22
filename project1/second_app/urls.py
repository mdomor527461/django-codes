from .views import courses
from django.urls import path
from .views import about
urlpatterns = [
    path('courses/',courses),
    path('about/',about)
]