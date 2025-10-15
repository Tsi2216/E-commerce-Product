# accounts/serializers.py 

from rest_framework import serializers
from django.contrib.auth import get_user_model

# Retrieves your Custom User Model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for displaying user details. 
    Removes 'username' to fix ImproperlyConfigured error.
    """
    class Meta:
        model = User
        # Removed 'username' and kept 'email' as the unique identifier
        fields = ['id', 'email', 'is_seller']
        read_only_fields = ['id', 'email'] # Made email read-only for safety


class RegisterSerializer(serializers.ModelSerializer):
    """
    Serializer for user registration.
    Adjusted to use 'email' instead of 'username' for creating the user.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        # Removed 'username' and only expose 'email' and 'password' for registration
        fields = ['email', 'password']

    def create(self, validated_data):
        # NOTE: If your custom User model requires a 'username' value 
        # (even if it's not used for login), you may need to set it 
        # here using the email, e.g., username=validated_data['email'].
        
        user = User.objects.create_user(
            # Using email as the primary unique identifier for creation
            email=validated_data['email'], 
            password=validated_data['password']
            # Removed the attempt to pass 'username'
        )
        return user