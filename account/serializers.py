from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    # p1 = serializers.CharField(min_length=8, max_length=20, required=True, write_only=True)
    p2 = serializers.CharField(min_length=8, max_length=20, required=True, write_only=True)

    class Meta:
        model = User
        fields = 'email', 'password', 'p2'

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('p2')

        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпали')
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    