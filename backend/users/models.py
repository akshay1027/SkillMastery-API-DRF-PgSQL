from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
import uuid


class TopicTag(models.Model):
    name = models.CharField(
        primary_key=True, max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name


# Skills are added by teh user to indicate topics they are proficient in
class SkillTag(models.Model):
    name = models.CharField(
        primary_key=True, max_length=150, null=False, blank=False)

    def __str__(self):
        return self.name


class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    profile_pic = models.ImageField(null=True, default="avatar.svg")
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


# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, null=True)
#     username = models.CharField(max_length=200, null=True)
#     profile_pic = models.ImageField(
#         blank=True, null=True, default='default.png')
#     bio = models.TextField(null=True)
#     # vote_ratio = models.IntegerField(blank=True, null=True, default=0)
#     # followers_count = models.IntegerField(blank=True, null=True, default=0)
#     skills = models.ManyToManyField(
#         SkillTag, related_name='personal_skills', blank=True)
#     interests = models.ManyToManyField(
#         TopicTag, related_name='topic_interests', blank=True)
#     # followers = models.ManyToManyField(
#     #     User, related_name='following', blank=True)
#     email_verified = models.BooleanField(default=False)
#     isTutor = models.BooleanField(default=False)
#     # id = models.UUIDField(default=uuid.uuid4,  unique=True,
#     #                       primary_key=True, editable=False)

    # def __str__(self):
    #     return str(self.user.username)
