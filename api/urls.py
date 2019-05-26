from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    path('', views.api_root),
    path('users/', views.UserList.as_view(), name='customuser-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='customuser-detail'),
    path('departments/', views.DepartmentList.as_view(), name='department-list'),
    path('departments/<int:pk>/', views.DepartmentDetail.as_view(), name='department-detail'),
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)