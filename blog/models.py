from django.db import models

# Create your models here.

class Author(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    
    def __str__(self):
        return self.firstName + " " + self.lastName

class Post(models.Model):
    title = models.CharField(max_length=100)
    article = models.CharField(max_length=2000)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publishedAt = models.DateTimeField()

    def __str__(self):
        return self.title
