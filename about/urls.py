from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.about_me, name='about'),
]