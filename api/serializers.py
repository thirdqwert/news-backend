from rest_framework import serializers
from .models import Category, News, Image


class NewsSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True, read_only=True)
    category_choose = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        many=True,
        write_only=True
    )
    preview_field = serializers.ImageField(write_only=True, required=True)

    def create(self, validated_data):
        image = validated_data.pop('preview_field')
        # сделать тут систему загрузки изображения на яндекс

        validated_data.update({'preview': str(image)})
        return super().create(validated_data)

    class Meta:
        model = News
        fields = ["id", "title", "category", "desc", "content", "news_views", "preview", "created_at", "category_choose", "preview_field"]
        read_only_fields = ["news_views", "created_at", "preview"]



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "title"]


class ImageSerializer(serializers.ModelSerializer):
    image_field = serializers.ImageField(write_only=True, required=True)
    
    def create(self, validated_data):
        image = validated_data.pop('image_field')
        # сделать тут систему загрузки изображения на яндекс
        validated_data.update({"image_link": image})
        return super().create(validated_data)

    class Meta:
        model = Image
        fields = ["id", "title", "image_link", "created_at", "image_field"]
        read_only_fields = ["image_link", "created_at"]