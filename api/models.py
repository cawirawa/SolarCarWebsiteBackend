from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from image_cropping import ImageRatioField

class OurTeam(models.Model):
    full_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=500)
    bio2 = models.TextField(max_length=500, blank=True, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=4)
    profile_header = models.CharField(max_length=150, null=True, blank=True)
    profile_image = models.ImageField(upload_to='images/%Y/%m/%d/', max_length=255, null=True, blank=True, default='https://i.stack.imgur.com/l60Hf.png')
    cropping = ImageRatioField('profile_image', '144x144')

class TeamPage(models.Model):
    header = models.CharField(max_length=100)
    content = models.CharField(max_length=500)

class NavBar(models.Model):
    name = models.CharField(max_length=20, unique=True)
    link = models.CharField(max_length=20, unique=True)

class Photo(models.Model):
    name = models.CharField(max_length=20, unique=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', null=False, blank=False)