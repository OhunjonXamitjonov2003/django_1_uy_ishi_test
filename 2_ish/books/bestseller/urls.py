from django.urls import path
from .views import sotuv_bolimi,sotuvchi,sayt,tuzuvchi

urlpatterns = [
    path('',sotuv_bolimi),
    path('sotuvchi/',sotuvchi),
    path('sayt/',sayt),
    path('tuzuvchi/',tuzuvchi),
]