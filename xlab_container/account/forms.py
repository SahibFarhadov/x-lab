from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Author

class register_user_form(ModelForm):
    class Meta():
        model = Author
        fields = ["email","password"]