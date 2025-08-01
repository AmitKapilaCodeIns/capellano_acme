"""
URL configuration for capellano_acme project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),  # URL for About app
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),  # Admin site URL
    path("summernote/", include("django_summernote.urls")),  # URL for Django Summernote
    path("", include("courseguide.urls"), name="courseguide-urls"),
]