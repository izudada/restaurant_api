from rest_framework import serializers

from .models import Menu

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'restaurant', 'dish', 'description', 'image_url', 'created_at']