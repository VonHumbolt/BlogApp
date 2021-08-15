from django.contrib.auth.models import User
from django.db import models
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default="profile.jpg", upload_to="profilePictures")

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name} Profile"

    def save(self):
        super().save()

        image = Image.open(self.image.path)
        if image.height > 300 or image.width > 300:
            image.thumbnail((300,300))
            image.save(self.image.path)