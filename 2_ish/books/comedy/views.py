from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def salom(request):
    return HttpResponse("Assalomu alaykum saytga hush kelibsiz!")

def about(request):
    return HttpResponse("biz haqimizda: +998911234567")

def sayt(request):
    return HttpResponse("bu books sayitidagi comedy bo'limi")

def tuzuvchi(request):
    return HttpResponse("sayt tuzuvchisi: Ohunjon Xamitjonov")