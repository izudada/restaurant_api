from rest_framework import serializers

from .models import Menu

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id', 'restaurant', 'dish', 'description', 'image_url', 'created_at']