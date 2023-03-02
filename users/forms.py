from dajngo import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
email = forms.EmailFiled()

class Meta:

    model = User
