from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('index',views.index,name='index'),
    path('blog/<slug:_slug>',views.yazini_tap,name='yazini_tap'),
]