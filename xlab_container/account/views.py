from django.shortcuts import render,redirect
from blog.models import Kateqoriya
from .forms import register_user_form
from .models import Author
from django.db import models
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

# reset password view
def _reset_password():
	pass

# register user
def _register_user(request):
	if request.method == "POST":
		email = request.POST["email"]
		password1 = request.POST["password1"]
		password2 = request.POST["password2"]
		if Author.objects.filter(email = email).exists():
			print("bu email ile qeydiyyat olunmusdur.")
		else:
			if password1 == password2:
				Author.objects.create_user(email=email,password=password1)
				return redirect("index")
	context = {
	'kateqoriyalar': Kateqoriya.objects.all(),
	'cari_sehife' : 'qeydiyyat',
	'form' : register_user_form(),
}
	return render(request,'account/register_user.html',context)

# user profile view
def _user_profile(request):
	pass