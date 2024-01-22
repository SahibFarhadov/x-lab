from django.shortcuts import render
from .models import Kateqoriya,Blog

# Create your views here.

def index(request):
    # cox oxunulan blogu sehifeye list olaraq gondereceyik
    # birincisi elementin ozu ikincisi novbeti elementin olub-olmadigini gosterecek
    cox_oxunulan_kateqoriya = Blog.objects.get(id=2).blog_kateqoriya.all()
    cox_oxunulan_kateqoriya_list = list()
    for element in cox_oxunulan_kateqoriya:
        cox_oxunulan_kateqoriya_list.append(list((element,True)))
    cox_oxunulan_kateqoriya_list[len(cox_oxunulan_kateqoriya_list)-1][1] = False

    context = {
        'kateqoriyalar': Kateqoriya.objects.all(),
        'yazilar' : Blog.objects.all(),
        'cox_oxunulan': Blog.objects.get(id=2),
        'cox_oxunulan_kateqoriya_list':cox_oxunulan_kateqoriya_list,
        'yeni_yazilar' : Blog.objects.filter(yeni_mi=True),
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