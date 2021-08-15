from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.contrib import messages
from users.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    form = UserRegisterForm()

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account has been created! Welcome {username}")
            return redirect(reverse("blog:home"))
    else: 
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form})


class LoginView(LoginView):
    template_name = "users/login.html"

class LogoutView(LogoutView):
    template_name = "users/logout.html"

@login_required
def profile(request):
    if request.method == "POST":
        userForm = UserUpdateForm(request.POST, instance=request.user)
        profileForm = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            profileForm.save()
            messages.success(request, "Your account has been updated")
            return redirect("users:profile")

    else:
        userForm = UserUpdateForm(instance=request.user)
        profileForm = ProfileUpdateForm(instance= request.user.profile)
    
    context = {
        "userForm" : userForm,
        "profileForm" : profileForm
    }

    return render(request, "users/profile.html", context)