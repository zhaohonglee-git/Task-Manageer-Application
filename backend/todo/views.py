from django.shortcuts import render

from rest_framework import viewsets
from .serializers import TodoSerializer
from rest_framework import permissions
from .models import Todo

# Create your views here.


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all().order_by('id')
    serializer_class = TodoSerializer
    permission_classes = [permissions.AllowAny]
    
