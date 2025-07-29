from django.urls import path

# from all import views
from . import views

# provide a list of URL patterns. Navigation to these URLs will be handled by the views defined in this module.
# This file is used to define the URL routing for the 'calc' app.
# Each path() function maps a URL to a specific view function.
urlpatterns = [
    path('', views.course_guide, name='course_guide'),  # Maps the root URL to the course_guide view
]