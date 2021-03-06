from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Permission to allow user to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """
        Override has object permission function
        Check if user is updating own profile
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == request.user.id