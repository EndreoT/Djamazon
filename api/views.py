from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UserSerializer, DepartmentSerializer, ProductSerializer
from .models import Department, Product


class UserList(generics.ListCreateAPIView):
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = get_user_model().objects.all()
  serializer_class = UserSerializer


class DepartmentList(generics.ListCreateAPIView):
  queryset = Department.objects.all()
  serializer_class = DepartmentSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

  def perform_create(self, serializer):
    serializer.save(created_by=self.request.user)


class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Department.objects.all()
  serializer_class = DepartmentSerializer
  permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class ProductList(generics.ListCreateAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Product.objects.all()
  serializer_class = ProductSerializer
