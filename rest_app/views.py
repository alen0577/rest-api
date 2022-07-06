from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView


# Create your views here.
class TaskViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all().order_by('-date_added')
    serializer_class = TaskSerializers


class CreateUserView(CreateAPIView):
    model = get_user_model()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class DueTaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_added').filter(completed=False)
    serializer_class = TaskSerializers


class CompletedTaskViewset(viewsets.ModelViewSet):
    queryset = Task.objects.all().order_by('-date_added').filter(completed=True)
    serializer_class = TaskSerializers
