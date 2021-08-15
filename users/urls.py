from django.urls import path
import users.views as userViews

app_name="users"

urlpatterns = [
    path("register/", userViews.register, name="register"),
    path("login/", userViews.LoginView.as_view(), name="login"),
    path("logout/", userViews.LogoutView.as_view(), name="logout"),
    path("profile/", userViews.profile, name="profile"),
]