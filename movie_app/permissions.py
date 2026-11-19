from rest_framework import permissions


class CheckStatus(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.status == 'pro':
            return True
        if request.user.status == 'simple' and view.action in ['list', 'retrieve']:
            return True
        return False


class CheckOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
