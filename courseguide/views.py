from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def course_guide(request):
    return HttpResponse("Welcome to the Course Guide!")
