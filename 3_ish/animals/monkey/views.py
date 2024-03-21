from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def salom(request):
    return HttpResponse("ANIMALS saytinig monkey bolimiga hush kelibsiz!!!")

def info(request):
    return HttpResponse("bu bolimda siz maymunlar haqida malumot olishingiz mumkin")

def text(request):
    return HttpResponse("Maymunlar uzun dum, qo‘l-oyoqlarga ega bo‘lgan yungli mavjudot hisoblanadi. Dunyoda ularning 260dan ortiq turlari mavjud\n"
    "Maymunlar dunyoda qayerda yashashlariga qarab, kopincha eski dunyo maymunlari va yangi dunyo maymunlariga bolinadi.")



def malumot(request):
    return HttpResponse("biz haqimizda: +998911234567")

def tuzuvchi(request):
    return HttpResponse("Tuzuvchi: Xamitjonov Ohunjon")