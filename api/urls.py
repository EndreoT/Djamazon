from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('departments/', views.DepartmentList.as_view()),
    path('departments/<int:pk>/', views.DepartmentDetail.as_view()),
]

# urlpatterns = format_suffix_patterns(urlpatterns)