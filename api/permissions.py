from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    message = "You must be the creater of this department for write access."
    def has_object_permission(self, request, view, obj):
      # Read permissions are allowed to any request,
      # so we'll always allow GET, HEAD or OPTIONS requests.
      if request.method in permissions.SAFE_METHODS:
        return True
      
      # Write permissions are only allowed to the owner of the department
      return obj.created_by == request.user


# class IsSuperUser(permissions.BasePermission):

#   def has_permission(self, request, view):
#     return obj.is_superuser

#   def has_object_permission(self, request, view, obj):
#     return obj.is_superuser