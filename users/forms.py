from users.models import Profile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ["image"]