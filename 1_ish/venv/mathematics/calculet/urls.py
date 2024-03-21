from django.urls import path
from.views import hello,about,amallar,info

urlpatterns = [
    path('',hello),
    path('about/',about),
    path('amallar/',amallar),
    path('info/',info),
]