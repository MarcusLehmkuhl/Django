from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# from django.shortcuts import render


def home(request):
    print('home')
    return HttpResponse('home do app 1')