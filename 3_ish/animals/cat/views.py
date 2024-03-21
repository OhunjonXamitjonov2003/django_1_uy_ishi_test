from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse



def salom(request):
    return HttpResponse("ANIMALS saytiga hush kelibsiz!!!")

def info(request):
    return HttpResponse("bu bolimda siz mushuklar haqida malumot olishingiz mumkin")

def text(request):
    return HttpResponse("loyihaning cat bolimi")



def malumot(request):
    return HttpResponse("1. Rivojlanish nuqtai nazaridan mushuk hayotining birinchi yili inson hayotining dastlabki 15 yiliga to‘g‘ri keladi")

def tuzuvchi(request):
    return HttpResponse("Tuzuvchi: Xamitjonov Ohunjon")
