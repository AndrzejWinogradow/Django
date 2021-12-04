from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_hello(request):
    return HttpResponse('No hejka')


def oferty(request):
    return HttpResponse('tu będą oferty')