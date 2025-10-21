# accounts/views.py

from rest_framework import viewsets, mixins, permissions # <-- IMPORT permissions
from .serializers import UserSerializer, RegisterSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class UserViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin
):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # -----------------------------------------------------------
    # FIX: Override get_permissions to allow anonymous registration
    # -----------------------------------------------------------
    def get_permissions(self):
        """
        Sets the permissions based on the requested action.
        Allows anonymous users for the 'create' (POST/registration) action.
        """
        if self.action == 'create':
            # Allow ANY user (anonymous or authenticated) to register
            self.permission_classes = [permissions.AllowAny]
        else:
            # Require authentication for all other actions (retrieve, update, etc.)
            self.permission_classes = [permissions.IsAuthenticated]
        
        # Instantiate and return the permission classes
        return [permission() for permission in self.permission_classes]

    # -----------------------------------------------------------
    # Original get_serializer_class method
    # -----------------------------------------------------------
    def get_serializer_class(self):
        if self.action == 'create':
            return RegisterSerializer
        return UserSerializer