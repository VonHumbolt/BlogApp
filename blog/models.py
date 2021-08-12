from django.db import models
from django.urls.base import reverse
from django.utils import timezone

# Create your models here.

class Author(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    
    def __str__(self):
        return self.firstName + " " + self.lastName

class Post(models.Model):
    title = models.CharField(max_length=100)
    article = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publishedAt = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:home")