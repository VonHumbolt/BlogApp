from typing import List
from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.
class HomeView(ListView):
    template_name= "blog/home.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.all()

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"
