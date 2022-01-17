from rest_framework.serializers import ModelSerializer
from ..models import UserProfile


class UserPorfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
