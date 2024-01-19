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
        'yazi':Blog.objects.get(blog_slug=_slug),
        'kateqoriyalar': Kateqoriya.objects.all(),
    }
    return render(request,'blog/yazini_tap.html',context)

# kateqoriyaya get.
def kateqoriyaya_get(request,_slug):
    context = {
        'kateqoriyalar': Kateqoriya.objects.all(),
        'yazilar' : Kateqoriya.objects.get(kateqoriya_slug =_slug).blog_set.all(),
        'secilen_kateqoriya' : Kateqoriya.objects.get(kateqoriya_slug=_slug),
    }
    return render(request,'blog/kateqoriyaya_get.html',context)