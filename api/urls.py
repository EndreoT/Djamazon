from django.urls import path, include
# from rest_framework.urlpatterns import format_suffix_patterns
# from api import views

from api.views import UserViewSet, DepartmentViewSet, ProductViewSet, GroupViewSet
# from rest_framework import renderers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# Create a router and register our viewsets with it
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'departments', DepartmentViewSet)
router.register(r'products', ProductViewSet)


# Entry point on /api is automatically generated
# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]



# # Url patterns using Viewset classes
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

# department_list = DepartmentViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# department_detail = DepartmentViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# product_list = ProductViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# product_detail = ProductViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })

# # Url pattenrns using Viewset classes
# urlpatterns = [
#     path('', api_root),
#     path('users/', user_list, name='customuser-list'),
#     path('users/<int:pk>/', user_detail, name='customuser-detail'),
#     path('departments/', department_list, name='department-list'),
#     path('department/<int:pk>/', department_detail, name='department-detail'),
#     path('products/', product_list, name='product-list'),
#     path('products/<int:pk>/', product_detail, name='product-detail'),
    
# ]

# Url pattenrns using View classes
# urlpatterns = [
#     path('', views.api_root),
#     path('users/', views.UserList.as_view(), name='customuser-list'),
#     path('users/<int:pk>/', views.UserDetail.as_view(), name='customuser-detail'),
#     path('departments/', views.DepartmentList.as_view(), name='department-list'),
#     path('departments/<int:pk>/', views.DepartmentDetail.as_view(), name='department-detail'),
#     path('products/', views.ProductList.as_view(), name='product-list'),
#     path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
# ]

# urlpatterns = format_suffix_patterns(urlpatterns)