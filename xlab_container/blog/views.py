from django.shortcuts import render
from .models import Kateqoriya,Blog

# Create your views here.

def index(request):
    context = {
        'kateqoriyalar': Kateqoriya.objects.all(),
        'yazilar' : Blog.objects.all(),
    }
    return render(request,'blog/index.html',context)

def yazini_tap(request,_slug):
    context = {
        'yazi':Blog.objects.get(blog_slug=_slug)
    }
    return render(request,'blog/yazini_tap.html',context)
    