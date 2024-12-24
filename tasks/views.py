from django.shortcuts import render ,redirect
from .models import Task

# Create your views here.

def home(request):
    return render(request,'home.html')

