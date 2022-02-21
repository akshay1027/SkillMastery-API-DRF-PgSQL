from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import uuid


class TopicTag(models.Model):
    name = models.CharField(
        primary_key=True, max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name


# Skills are added by the user to indicate topics they are proficient in
class SkillTag(models.Model):
    name = models.CharField(
        primary_key=True, max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = models.CharField(max_length=200, null=True, unique=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    profile_pic = models.ImageField(
        null=True, default="https://i.stack.imgur.com/y9DpT.jpg")
    skills = models.ManyToManyField(
        SkillTag, related_name='personal_skills', blank=True)
    interests = models.ManyToManyField(
        TopicTag, related_name='topic_interests', blank=True)
    email_verified = models.BooleanField(default=False)
    isTutor = models.BooleanField(default=False)
    id = models.UUIDField(default=uuid.uuid4,  unique=True,
                          primary_key=True, editable=False)

    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
