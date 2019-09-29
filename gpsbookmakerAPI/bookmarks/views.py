from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views import View
from django.shortcuts import render
from rest_framework import serializers, generics, viewsets, mixins, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from bookmarks.models import Bookmark
from bookmarks.serializers import BookmarkSerializer
# from rest_framework import routers, serializers, viewsets


# Create your views here.
class OwnerOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request: HttpRequest, view: View, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        owns_object = (obj.user == request.user)
        # Write permissions are only allowed to the owner of the snippet.
        return owns_object

# class AllowAnyone(permissions.BasePermission):

#     def has_permission(self, request: HttpRequest, view: View):
#         return True

#     def has_object_permission(self, request: HttpRequest, view: View, obj):
#         return True

class BookmarkViewSet(mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      mixins.ListModelMixin,
                      GenericViewSet):
    permission_classes =  (permissions.DjangoModelPermissions, OwnerOnly)
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)
