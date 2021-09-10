# from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def home(request):
    return HttpResponse('127.0.0.1 sweet 127.0.0.1')
