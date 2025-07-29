from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(
        request,
        'calc/home.html',
        {
            'name': 'Capellano',
        }
    )  # Render the home template for the calc app
# render means you need to render a template, that contains static and dynamic content.


def add(request):
        num1 = int(request.POST["num1"])  # Get the first number from the GET request
        num2 = int(request.POST["num2"])  # Get the second number from the GET request
        
        result = num1 + num2  # Calculate the sum
        return render(
            request,
            'calc/result.html',
            {
                'num1': num1,
                'num2': num2,
                'result': result
            }  # Pass the result to the result template
        )