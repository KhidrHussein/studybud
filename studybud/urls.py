
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(response):
    return HttpResponse("Home page")


def room(response):
    return HttpResponse('Room')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls'))
]
