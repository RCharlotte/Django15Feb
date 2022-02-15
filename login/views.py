from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def login(request):
    return HttpResponse("Sample login page")



