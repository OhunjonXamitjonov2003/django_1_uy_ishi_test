from django.urls import path,include
from .views import detectiv,malumot,info,tuzuvchi
urlpatterns = [
    path('',detectiv),
    path('malumot/',malumot),
    path('info/',info),
    path('tuzuvchi',tuzuvchi),
]