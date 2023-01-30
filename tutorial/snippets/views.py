from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import UserSerializer, SignUpSerializer, VideoSerializer, PostSerializer
from rest_framework.response import Response
from .models import Video 
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from knox.auth import TokenAuthentication
from knox.views import LoginView as KnoxLoginView
from rest_framework.authentication import BasicAuthentication
from rest_framework.authtoken.models import Token
class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication]
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # authentication_classes = [JSONWebTokenAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    
class SignupViewSet(viewsets.ModelViewSet):
    serializer_class = SignUpSerializer
    queryset = User.objects.all()
    # authentication_classes = [JSONWebTokenAuthentication]
    
class VideoViewSet(viewsets.ModelViewSet):
    serializer_class = VideoSerializer
    queryset = Video.objects.all()
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [JSONWebTokenAuthentication]
    # def perform_create(self, serializer):
    #     serializer.save(file=self.request.data.get('file'))
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Video.objects.all()
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]