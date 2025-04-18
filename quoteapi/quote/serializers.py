from rest_framework import serializers
from .models import Quote
from django.contrib.auth.models import User

class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['id', 'text', 'author', 'is_public', 'owner', 'created_at']
        read_only_fields = ['owner', 'created_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only' : True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username = validated_data['username'],
            password = validated_data['password'],
        )
        return user