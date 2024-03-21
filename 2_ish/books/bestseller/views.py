from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def sotuv_bolimi(request):
    return HttpResponse("Assalomu alaykum sotuv bo'limiga hush kelibsiz!")

def sotuvchi(request):
    return HttpResponse("sotuvchiga murojat: +998911234567")

def sayt(request):
    return HttpResponse("bu books sayitidagi bestseller bo'limi")

def tuzuvchi(request):
    return HttpResponse("tuzuvchi:Xamitjanov Ohunjon")