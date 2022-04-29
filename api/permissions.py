from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        #allow read-only permissions for all requests
        if request.method in permissions.SAFE_METHODS: 
            return True

        #allow write permissions to author of a post/currently logged in user
        return obj.author == request.user