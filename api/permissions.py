from rest_framework import permissions


class IsCustomer(permissions.BasePermission):

  def has_permission(self, request, view):
    return request.user.groups.filter(name='Customer').exists()

  def has_object_permission(self, request, view, obj):
    return request.user.groups.filter(name='Customer').exists()


class IsSupervisor(permissions.BasePermission):

  def has_permission(self, request, view):
    return request.user.groups.filter(name='Supervisor').exists()

  def has_object_permission(self, request, view, obj):
    return request.user.groups.filter(name='Supervisor').exists()


class IsSupervisorOrReadOnly(permissions.BasePermission):

  def has_permission(self, request, view):
    if request.method in permissions.SAFE_METHODS:
        return True
    return request.user.groups.filter(name='Supervisor').exists()

  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
        return True
    return request.user.groups.filter(name='Supervisor').exists()


class IsManager(permissions.BasePermission):

  def has_permission(self, request, view):
    return request.user.groups.filter(name='Manager').exists()

  def has_object_permission(self, request, view, obj):
    return request.user.groups.filter(name='Manager').exists()


class IsManagerOrReadOnly(permissions.BasePermission):
  """
    Custom permission to only allow managers write access to object
  """
  message = "You must be the creater of this department for write access."
  def has_permission(self, request, view):
    # Read permissions are allowed to any request,
    # so we'll always allow GET, HEAD or OPTIONS requests.
    if request.method in permissions.SAFE_METHODS:
        return True
    # Write permissions are only allowed to managers
    return request.user.groups.filter(name='Manager').exists()

  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
        return True
    return request.user.groups.filter(name='Manager').exists()


