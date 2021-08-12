from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Author
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# Create your views here.
class HomeView(ListView):
    template_name= "blog/home.html"
    context_object_name = "posts"
    ordering = ["-publishedAt"]

    def get_queryset(self):
        return Post.objects.all()

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "article"]

    def form_valid(self, form):
        form.instance.author = Author.objects.get(pk=self.request.user.id)
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "article"]
    
    def form_valid(self,form):
        form.instance.author = Author.objects.get(pk = self.request.user.id)
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
    
        if Author.objects.get(pk = self.request.user.id) == post.author:
            return True
        return False 
