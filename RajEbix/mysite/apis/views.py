from django.shortcuts import render

# Create your views here.
from mypost.models import Posts
from rest_framework import serializers, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"


class UserViewSet(viewsets.ModelViewSet):
	
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

