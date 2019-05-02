from django.shortcuts import render
from .models import Blog

def layout(request):
    return render(request, 'layout.html')

def home(request):  
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs' : blogs})