from django.urls import path
from .views import HomeView, PostDeleteView, PostDetailView, PostCreateView, PostUpdateView

app_name="blog"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("add/", PostCreateView.as_view(), name="post-create"),
    path("<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
]
