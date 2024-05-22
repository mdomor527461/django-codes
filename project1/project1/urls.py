from .view import contact
from django.contrib import admin
from django.urls import path,include
from .view import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/',contact),
    path('',home),
    path("first_app",include("first_app.urls")),
    path("second_app/",include("second_app.urls"))
]
