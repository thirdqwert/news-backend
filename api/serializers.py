import io
import pillow_avif
from datetime import datetime
from rest_framework import serializers
from .models import Category, News, Image, Article, Audio, Album
from PIL import Image as Pillow_Image
from django.core.files.base import ContentFile



def save_image(input_image, title):
    # Функция конвертирование и сохранение изображений 
    img = Pillow_Image.open(input_image)
    buffer = io.BytesIO()
    img.save(buffer, format="AVIF", quality=60)
    file_name = f"{title + str(datetime.now())}.avif"
    django_file = ContentFile(buffer.getvalue(), name=file_name)

    return django_file



class NewsSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True, read_only=True)
    category_choose = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        many=True,
        write_only=True
    )

    def create(self, validated_data):
        input_image = validated_data.pop("preview")
        file = save_image(input_image, validated_data.get('title'))
        validated_data.update({ "preview": file })

        return super().create(validated_data)

    class Meta:
        model = News
        fields = ["id", "title", "short_title", "category", "desc", "content", "news_views", "preview", "created_at", "category_choose",]
        read_only_fields = ["news_views", "created_at",]


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True, read_only=True)
    category_choose = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        many=True,
        write_only=True
    )

    def create(self, validated_data):
        input_image = validated_data.pop("preview")
        file = save_image(input_image=input_image, title=validated_data.get('title'))
        validated_data["preview"] = file

        return super().create(validated_data)

    class Meta:
        model = Article
        fields = ["id", "title", "short_title", "category", "desc", "content", "article_views", "preview", "created_at", "category_choose"]
        read_only_fields = ["article_views", "created_at"]


class AlbumSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True, read_only=True)
    category_choose = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        many=True,
        write_only=True
    )

    def create(self, validated_data):
        input_image = validated_data.pop("preview")
        file = save_image(input_image=input_image, title=validated_data.get('title'))
        validated_data["preview"] = file

        return super().create(validated_data)

    class Meta:
        model = Album
        fields = ["id", "title", "short_title", "category", "desc", "content", "album_views", "preview", "created_at", "category_choose"]
        read_only_fields = ["album_views", "created_at"]


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "title"]


class ImageSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        input_image = validated_data.pop("image")
        file = save_image(input_image=input_image, title=validated_data.get('title'))
        validated_data.update({"image": file})

        return super().create(validated_data)

    class Meta:
        model = Image
        fields = ["id", "title", "image", "created_at"]
        read_only_fields = ["created_at"]


class AudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Audio
        fields = ["id", "title", "audio", "created_at"]
        read_only_fields = ["created_at"]
