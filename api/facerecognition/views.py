from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from api.facerecognition.serializers import UserSerializer, GroupSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import authentication, permissions

import pdb;
import os
import face_recognition


class UserViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  """
  queryset = User.objects.all().order_by('-date_joined')
  serializer_class = UserSerializer
  permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows groups to be viewed or edited.
  """
  queryset = Group.objects.all()
  serializer_class = GroupSerializer
  permission_classes = [permissions.IsAuthenticated]


class facerecognitionAPIView(APIView):
  """
  Output should be either person ID if it matches in our database or null if no match . 
  """
  # permission_classes = [permissions.IsAdminUser]
  permission_classes = [permissions.IsAuthenticated]

  def get(self, request):
    """
    Return a list of all users.
    """
    folder_name = request.GET.get('params', '')
    stream = os.popen(f'face_recognition ./api/facerecognition/img/known/{folder_name} ./api/facerecognition/img/unknown')
    output = stream.read()
    # print(output)
    # usernames = []
    return Response(output.split('\n'))
