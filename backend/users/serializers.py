from rest_framework import serializers
# from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User, TopicTag, SkillTag


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
    interests = TopicTagSerializer(many=True, read_only=True)
    skills = SkillTagSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def get_profile_pic(self, obj):
        try:
            pic = obj.profile_pic.url
        except:
            pic = None
        return pic


class CurrentUserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email']

    # def get_profile(self, obj):
    #     profile = obj.userprofile
    #     serializer = UserProfileSerializer(profile, many=False)
    #     return serializer.data


class UserSerializer(serializers.ModelSerializer):
    profile = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username']

    # def get_profile(self, obj):
    #     profile = obj.userprofile
    #     serializer = UserProfileSerializer(profile, many=False)
    #     return serializer.data


# regsuter user
class UserSerializerWithToken(UserSerializer):
    print('here')
    access = serializers.SerializerMethodField(read_only=True)
    refresh = serializers.SerializerMethodField(read_only=True)

    class Meta:
        print('here meta')
        model = User
        exclude = ['password']

    def get_profile(self, obj):
        print('object =', obj)
        serializer = UserProfileSerializer(obj, many=False)
        return serializer.data

    def get_access(self, obj):
        print('isnide function')
        token = RefreshToken.for_user(obj)

        token['username'] = obj.username
        # token['name'] = obj.userprofile.name
        # token['profile_pic'] = obj.userprofile.profile_pic.url
        # token['is_staff'] = obj.is_staff
        token['id'] = str(obj.id)
        # print()
        return str(token.access_token)

    def get_refresh(self, obj):

        token = RefreshToken.for_user(obj)
        return str(token)
