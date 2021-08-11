from django.shortcuts import redirect, render
from django.urls.base import reverse
from django.contrib import messages
from users.forms import UserRegisterForm
from django.contrib.auth.views import LoginView, LogoutView

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
