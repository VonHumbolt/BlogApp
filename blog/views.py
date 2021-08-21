from django.shortcuts import get_object_or_404, render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Author
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

def introView(request):
    return render(request, "blog/intro.html", {})

class HomeView(ListView):
    template_name= "blog/home.html"
    context_object_name = "posts"
    ordering = ["-publishedAt"]
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.all()

class AuthorPostsListView(ListView):
    model = Post
    template_name = "blog/author_post.html"
    context_object_name = "posts"
    paginate_by = 3
    
    def get_queryset(self):
        authorId = self.kwargs.get("pk")
        return Post.objects.filter(author_id = authorId).order_by("-publishedAt")

class PostDetailView(DetailView):
    model = Post
    template_name = "blog/detail.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "article", "postImage"]

    def form_valid(self, form):
        form.instance.author = Author.objects.get(user_id=self.request.user.id)
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "article", "postImage"]

    def form_valid(self,form):
        form.instance.author = Author.objects.get(user_id = self.request.user.id)
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user.id == post.author.user.id:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blog/post_delete.html"
    success_url = "/"

    def test_func(self):
        post = self.get_object()

        if self.request.user.id == post.author.user.id:
            return True
        return False


def filterPost(request):
    filterType = request.GET["selected"]
    query = request.GET["searchInput"]
    
    if filterType == "author":
        if " " in query:
            [firstName, lastName] = query.split(" ")
            author = Author.objects.filter(user__first_name__icontains=firstName, user__last_name__icontains=lastName).first()
        else:
            author = Author.objects.filter(user__first_name__icontains=query).first()
        
        posts = Post.objects.filter(author = author)

    elif filterType == "title":
        posts = Post.objects.filter(title__icontains =query)
    else:
        posts = Post.objects.filter(article__icontains = query)

    return render(request, "blog/home.html", {"posts":posts})
