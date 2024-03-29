from django.urls import path
from . import views

urlpatterns = [
	path('login',views._login_user,name='login_user'),
	path('register',views._register_user,name='register_user'),
	path('user_profile',views._user_profile,name='user_profile'),
	path('reset_password',views._reset_password,name='reset_password'),
	path('logout',views._logout_user,name='logout_user'),
	path('verify/<uuid:_uuid>',views.verify_email,name='verify_email'),
]