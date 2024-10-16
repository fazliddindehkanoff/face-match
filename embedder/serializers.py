from rest_framework import serializers
from .models import Image, Embed


class ImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("image",)


class EmbedSerializer(serializers.ModelSerializer):
    images = ImageUploadSerializer(many=True, read_only=True)

    class Meta:
        model = Embed
        fields = ("id", "embedding", "organization", "created_at", "images")


class FaceCompareSerializer(serializers.Serializer):
    image = serializers.ImageField()
    organization = serializers.IntegerField()
