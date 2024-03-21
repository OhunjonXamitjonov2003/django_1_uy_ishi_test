
from django.urls import path
from .views import salom,info,text,malumot,tuzuvchi
urlpatterns = [
    path('',salom),
    path('info/',info),
    path('text/',text),
    path('malumot',malumot),
    path('tuzuvchi',tuzuvchi),

]
