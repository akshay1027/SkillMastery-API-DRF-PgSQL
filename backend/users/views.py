from asyncio.windows_events import NULL
import datetime
from email.policy import HTTP
from multiprocessing import AuthenticationError
import uuid
import random
import os.path

from django.contrib.auth.hashers import make_password
# from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.files.storage import default_storage
# from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.db.models import Q, Count
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from email_validator import validate_email, EmailNotValidError
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import User, SkillTag, TopicTag
from .serializers import (UserSerializerWithToken, UserSerializer)
from backend.users import serializers


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Add custom claims
        token['username'] = user.username

        return token


# Register user
# get the data -> check if data is valid -> save to db
class RegisterUser(APIView):
    permission_classes = [permissions.AllowAny]
    Authentication_classes = []

    def post(self, request):
        data = request.data
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        # email_valid_check_result = email_validator(email)
        messages = {'errors': []}

        if username == None:
            messages['errors'].append('username can\'t be empty')
        if email == None:
            messages['errors'].append('Email can\'t be empty')
        # if not email_valid_check_result == email:
        #     messages['errors'].append(email_valid_check_result)
        if password == None:
            messages['errors'].append('Password can\'t be empty')

        if User.objects.filter(email=email).exists():
            messages['errors'].append(
                "Account already exists with this email id.")
        if User.objects.filter(username__iexact=username).exists():
            messages['errors'].append(
                "Account already exists with this username.")

        if len(messages['errors']) > 0:
            return Response({"detail": messages['errors']}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.create(
                username=username,
                email=email,
                password=make_password(password),
            )
            print('user created')
            serializer = UserSerializerWithToken(user, many=False)
            print(serializer.data)
        except Exception as e:
            print(e)
            return Response({'detail': f'{e}'}, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.data, status=status.HTTP_200_OK)


# Get all users with pagination (max 10 per request)
@api_view(['GET'])
def users(request):
    # get the query from api endpoint, here no query hence its '', which will return all the values
    query = request.query_params.get('q') or ''
    # filter them
    users = User.objects.filter(
        Q(name__icontains=query) |
        Q(username__icontains=query)
    )
    print('here mate')
    paginator = PageNumberPagination()
    paginator.page_size = 8
    result_page = paginator.paginate_queryset(users, request)
    serializer = UserSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


# Login user
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


# User Details
@api_view(['GET'])
def UserDetails(request, username):
    user = User.objects.get(username=username)

    serializer = UserSerializer(user, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


# User recommendation system
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def users_recommended(request):
    user = request.user
    users = User.objects.annotate(followers_count=Count('userprofile__followers')).order_by(
        'followers_count').reverse().exclude(id=user.id)[0:5]
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
