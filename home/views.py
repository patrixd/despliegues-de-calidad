from django.shortcuts import render
from django.conf import settings


# Create your views here.

def home_view(request):
    template = 'index.html'
    return render(request, template, {'environment_name': settings.ENVIRONMENT_NAME})
