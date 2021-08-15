from django.db import models
from django.urls.base import reverse
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

class Post(models.Model):
    title = models.CharField(max_length=100)
    article = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    postImage = models.ImageField(default="placeholder.jpg", upload_to="postImages")
    publishedAt = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:home")