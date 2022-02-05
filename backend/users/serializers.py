from dataclasses import fields
from rest_framework import serializers
# from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, TopicTag, SkillTag

# if we are using serializers.ModelSerializer, we need to use model name and then serializer (conviction)


class TopicTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicTag
        fields = '__all__'


class SkillTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillTag
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    profile_pic = serializers.SerializerMethodField(read_only=True)
    # interests = TopicTagSerializer(many=True, read_only=True)
    # skills = SkillTagSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'profile_pic']

    def get_profile_pic(self, obj):
        try:
            pic = obj.profile_pic.url
        except:
            pic = None
        return pic


class CurrentUserSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email']

    def get_profile(self, obj):
        profile = obj.userprofile
        serializer = UserProfileSerializer(profile, many=False)
        return serializer.data


# Get all users
class UserSerializer(serializers.ModelSerializer):
    # username = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'id', 'isTutor',
                  'profile_pic', 'skills', 'interests']

    # def get_username(self, obj):
    #     profile = obj
    #     serializer = UserProfileSerializer(profile, many=False)
    #     return serializer.data


# register user
class UserSerializerWithToken(UserSerializer):
    # print('here')
    access = serializers.SerializerMethodField(read_only=True)
    refresh = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        exclude = ['password']

    def get_access(self, obj):
        # print('isnide function')
        token = RefreshToken.for_user(obj)

        token['username'] = obj.username
        token['id'] = str(obj.id)
        return str(token.access_token)

    def get_refresh(self, obj):

        token = RefreshToken.for_user(obj)
        return str(token)
