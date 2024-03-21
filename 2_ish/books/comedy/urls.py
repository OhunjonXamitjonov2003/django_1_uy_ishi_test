from django.urls import path
from .views import salom,about,sayt,tuzuvchi

urlpatterns = [
    path("",salom),
    path('about/',about),
    path('sayt/',sayt),
    path('tuzuvchi/',tuzuvchi),
]