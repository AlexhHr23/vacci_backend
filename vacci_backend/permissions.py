from rest_framework import permissions

class isUserORReadOnly(permissions.BasePermission):
    def has_objecto_permissions(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user