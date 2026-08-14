from rest_framework import serializers
from .models import User, Rol

class UserSerializer(serializers.ModelSerializer):

    role = serializers.SlugRelatedField(
        slug_field="code",
        queryset=Rol.objects.all()
    )
    class Meta:
        model = User
        fields = ['email', 'password' 'name', 'paternal_last_name', 'maternal_last_name', 'phone', 'role']

        extra_kwargs = {
            'password': {'write_only': True}
        }   

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)