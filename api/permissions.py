from rest_framework import permissions


class IsCustomer(permissions.BasePermission):
    message = "You must be a customer for any access."

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Customer').exists()

    def has_object_permission(self, request, view, obj):
        return request.user.groups.filter(name='Customer').exists()


class IsSupervisor(permissions.BasePermission):
    message = "You must be a supervisor for any access."

    def has_permission(self, request, view):
        return request.user.groups.filter(name='Supervisor').exists()

    def has_object_permission(self, request, view, obj):
        return request.user.groups.filter(name='Supervisor').exists()


class IsSupervisorOrReadOnly(permissions.BasePermission):

    message = "You must be a supervisor for write access."

    def permission_helper(self, request):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.groups.filter(name='Supervisor').exists()

    def has_permission(self, request, view):
        return self.permission_helper(request)

    def has_object_permission(self, request, view, obj):
        return self.permission_helper(request)


class IsManager(permissions.BasePermission):

    message = "You must be a manager for any access."

    def permission_helper(self, request):
        return request.user.groups.filter(name='Manager').exists()

    def has_permission(self, request, view):
        return self.permission_helper(request)

    def has_object_permission(self, request, view, obj):
        return self.permission_helper(request)


class IsManagerOrReadOnly(permissions.BasePermission):
    """
      Custom permission to only allow managers write access to object
    """
    message = "You must be a manager for write access."

    def permission_helper(self, request):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Write permissions are only allowed to managers
        return request.user.groups.filter(name='Manager').exists()

    def has_permission(self, request, view):
        return self.permission_helper(request)

    def has_object_permission(self, request, view, obj):
        return self.permission_helper(request)
