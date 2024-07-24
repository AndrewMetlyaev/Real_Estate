from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user


class IsRenterOrLandlord(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if view.action in ['list', 'retrieve']:

                return True

            elif view.action == 'create':

                return request.user.is_renter or request.user.is_staff

            elif view.action in ['update', 'partial_update', 'destroy']:

                return request.user == view.get_object() or request.user.is_staff

        return False
