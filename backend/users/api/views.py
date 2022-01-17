# Create your views here.
# we need decorators as its function based views and not class based

from django.http import JsonResponse
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated


from .serializers import UserPorfileSerializer
from ..models import UserProfile


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)


# @api_view(['GET'])
# def getNotes(request):
#     user = request.user
#     notes = user.note_set.all()
#     serializer = NoteSerializer(notes, many=True)
#     return Response(serializer.data)
