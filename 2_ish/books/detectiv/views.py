from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def detectiv(request):
    return HttpResponse("Assalomu alaykum saytning detectiv bolimiga hush kelibsiz")

def malumot(request):
    return HttpResponse("Bu bo'limda siz detictiv janrda yozilgan kitoblarni topishingiz mumkin")


def info(request):
    return HttpResponse('kitobni tanlab bolib sotuv bolimiga oting <a href="betseller/">Betseller</a>')

def tuzuvchi(request):
    return HttpResponse('tuzuvchi: Xamitjonov Ohunjon')