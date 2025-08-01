from django.shortcuts import render
from .models import About

# Create your views here.
def about_me(request):
    """
    Render the 'about me' page with information about the site author.
    """

    about = About.objects.all().order_by('-updated_on').first()
    return render(request, 'about/about.html', {'about': about})