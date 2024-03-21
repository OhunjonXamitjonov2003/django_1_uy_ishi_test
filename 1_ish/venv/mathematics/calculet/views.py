from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hello(request):
    return HttpResponse("Saytga hush kelibsiz!!!")

def about(request):
    return HttpResponse("sayt tuzuvchisi: +998911234567")

def amallar(request):
    return HttpResponse("Matematik amallar:(+,-,*,/")

def info(request):
    return HttpResponse("bu sayt test uchun tuzildi")