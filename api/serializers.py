from rest_framework import serializers
from .models import Category, Subcategory, News, Image, Article, Audio, Album
from .utils import save_image


class NewsSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    category_choose = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True
    )

    subcategory = serializers.StringRelatedField(read_only=True)
    subcategory_choose = serializers.PrimaryKeyRelatedField(
        queryset=Subcategory.objects.all(),
        source="subcategory",
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
        fields = ["id", "title", "short_title", "category", "subcategory", "desc", "content", "views", "preview", "created_at", "category_choose", "subcategory_choose"]
        read_only_fields = ["views", "created_at",]


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    category_choose = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True
    )

    subcategory = serializers.StringRelatedField(read_only=True)
    subcategory_choose = serializers.PrimaryKeyRelatedField(
        queryset=Subcategory.objects.all(),
        source="subcategory",
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
        fields = ["id", "title", "short_title", "category", "subcategory", "desc", "content", "views", "preview", "created_at", "category_choose", "subcategory_choose"]
        read_only_fields = ["views", "created_at"]


class AlbumSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(read_only=True)
    category_choose = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True
    )
    
    subcategory = serializers.StringRelatedField(read_only=True)
    subcategory_choose = serializers.PrimaryKeyRelatedField(
        queryset=Subcategory.objects.all(),
        source="subcategory",
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
        fields = ["id", "title", "short_title", "category", "subcategory", "desc", "content", "views", "preview", "created_at", "category_choose", "subcategory_choose"]
        read_only_fields = ["views", "created_at"]

# Доделай subcategory и удали category create
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "title", "slug"]


class SubcategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subcategory
        fields = ["id", "title","category", "slug"]


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


class SearchResultSerializer(serializers.Serializer):
    title = serializers.CharField()
    short_title = serializers.CharField()
    desc = serializers.CharField()
    content = serializers.CharField()
    views = serializers.IntegerField()
    preview = serializers.ImageField()
    created_at = serializers.DateTimeField()