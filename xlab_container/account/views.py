from django.shortcuts import render
from blog.models import Kateqoriya

# login user
def _login_user(request):
	context = {
        'kateqoriyalar': Kateqoriya.objects.all(),
        'cari_sehife' : 'daxil_ol'
    }
	return render(request,'account/login_user.html',context)

# logout user
def _logout_user(request):
	pass

# register user
def _register_user(request):
	context = {
        'kateqoriyalar': Kateqoriya.objects.all(),
        'cari_sehife' : 'qeydiyyat'
    }
	return render(request,'account/register_user.html',context)

# user profile view
def _user_profile(request):
	pass