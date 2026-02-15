from rest_framework import serializers
from .models import Category, News, Image, Article, Audio, Album
from .utils import save_image


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
    
    def update(self, instance, validated_data):
        input_image = validated_data.pop("preview", None)

        if input_image is not None:
            file = save_image(input_image, validated_data.get('title'))
            validated_data.update({ "preview": file })

        return super().update(instance, validated_data)

    class Meta:
        model = News
        fields = ["id", "title", "short_title", "category", "desc", "content", "views", "preview", "created_at", "category_choose",]
        read_only_fields = ["views", "created_at",]


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
    
    def update(self, instance, validated_data):
        input_image = validated_data.pop("preview", None)
        
        if input_image is not None:
            file = save_image(input_image, validated_data.get('title'))
            validated_data.update({ "preview": file })

        return super().update(instance, validated_data)

    class Meta:
        model = Article
        fields = ["id", "title", "short_title", "category", "desc", "content", "views", "preview", "created_at", "category_choose"]
        read_only_fields = ["views", "created_at"]


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
    
    def update(self, instance, validated_data):
        input_image = validated_data.pop("preview", None)
        
        if input_image is not None:
            file = save_image(input_image, validated_data.get('title'))
            validated_data.update({ "preview": file })

        return super().update(instance, validated_data)

    class Meta:
        model = Album
        fields = ["id", "title", "short_title", "category", "desc", "content", "views", "preview", "created_at", "category_choose"]
        read_only_fields = ["views", "created_at"]


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
    
    def update(self, instance, validated_data):
        input_image = validated_data.pop("preview", None)
        
        if input_image is not None:
            file = save_image(input_image, validated_data.get('title'))
            validated_data.update({ "preview": file })

        return super().update(instance, validated_data)

    class Meta:
        model = Image
        fields = ["id", "title", "image", "created_at"]
        read_only_fields = ["created_at"]


class AudioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Audio
        fields = ["id", "title", "audio", "created_at"]
        read_only_fields = ["created_at"]
