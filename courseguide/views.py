from django.shortcuts import render
from django.views import generic
from .models import Course

# Create your views here.


class CourseList(generic.ListView):
    queryset = Course.objects.all()  # Only show published courses
    template_name = 'courseguide/index.html'  # Template to render the course list
