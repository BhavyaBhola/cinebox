from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='profile_images' , default="blank_profile_pic.jpg")

    def __str__(self):
        return self.user.username