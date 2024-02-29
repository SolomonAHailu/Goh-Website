from django.shortcuts import render
from rest_framework import permissions, viewsets
from blogs.models import Blog
from blogs.permissions import IsAdminOrReadOnly
from blogs.serializers import (BlogReadSerializer, BlogWriteSerializer)


class BlogViewSet(viewsets.ModelViewSet):
    
    queryset = Blog.objects.all()
    def get_serializer_class(self):
        if self.action in ("create", "update", "partial_update", "destroy"):
            return BlogWriteSerializer
        return BlogReadSerializer
    def get_permissions(self):
        if self.action in ("create","update", "partial_update", "destroy"):
            self.permission_classes = (IsAdminOrReadOnly,)
        else:
            self.permission_classes = (permissions.AllowAny,)

        return super().get_permissions()