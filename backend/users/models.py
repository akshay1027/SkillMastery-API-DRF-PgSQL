from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    username = models.CharField(max_length=200, null=True)
    # profile_pic = models.ImageField(
    #     blank=True, null=True, default='default.png')
    bio = models.TextField(null=True)
