from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField(max_length=200)
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(write_only = True)
    phone_number = serializers.CharField(max_length=15)
    address = serializers.CharField(max_length=300)
    profile_image = serializers.URLField()
    active = serializers.ReadOnlyField()

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

class CustomUserDetailSerializer(CustomUserSerializer):
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.address = validated_data.get('address', instance.address)
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.date_updated = validated_data.get('date_updated', instance.date_updated)
        instance.save()
        return instance