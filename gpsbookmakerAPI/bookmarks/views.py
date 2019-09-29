from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import serializers, generics, viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
# from rest_framework import routers, serializers, viewsets
from bookmarks.models import Bookmark


# Create your views here.
class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('lat', 'lon', 'user')

class BookmarkViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
                           
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
