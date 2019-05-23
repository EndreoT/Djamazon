from rest_framework import generics
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, DepartmentSerializer
from .models import Department


class UserList(generics.ListCreateAPIView):
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer


class DepartmentList(generics.ListCreateAPIView):
  queryset = Department.objects.all()
  serializer_class = DepartmentSerializer


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Department.objects.all()
  serializer_class = DepartmentSerializer