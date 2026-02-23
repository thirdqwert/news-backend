from rest_framework import serializers
from .models import Category, Subcategory, News, Image, Audio, Reel
from .utils import save_image


class SubcategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Subcategory
        fields = ["id", "title","category", "slug"]


class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ["id", "title", "slug", "subcategories"]


class NewsSerializer(serializers.ModelSerializer):
    def get_categery_slug(self, obj):
        return obj.category.slug
    
    def get_subcategory_slug(self, obj):
        return obj.subcategory.slug or None

    category = serializers.StringRelatedField(read_only=True)
    category_choose = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source="category",
        write_only=True
    )
    categery_slug = serializers.SerializerMethodField(method_name="get_categery_slug")

    subcategory = serializers.StringRelatedField(read_only=True)
    subcategory_choose = serializers.PrimaryKeyRelatedField(
        queryset=Subcategory.objects.all(),
        source="subcategory",
        write_only=True,
        required=False
    )
    subcategory_slug = serializers.SerializerMethodField(method_name="get_subcategory_slug")

    def create(self, validated_data):
        input_image = validated_data.pop("preview")
        file = save_image(input_image)
        validated_data.update({ "preview": file })

        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        input_image = validated_data.pop("preview", None)

        if input_image is not None:
            file = save_image(input_image)
            validated_data.update({ "preview": file })

        return super().update(instance, validated_data)

    def get_categery_slug(self, obj):
        return obj.category.slug
    
    def get_subcategory_slug(self, obj):
        if obj.subcategory is not None:
            return obj.subcategory.slug
        return None

    class Meta:
        model = News
        fields = ["id", "title", "short_title", "category", "categery_slug", "subcategory", "subcategory_slug", "desc", "content", "views", "preview", "created_at", "category_choose", "subcategory_choose"]
        read_only_fields = ["views", "created_at", "categery_slug", "subcategory_slug",]


# class ArticleSerializer(serializers.ModelSerializer):
#     category = serializers.StringRelatedField(read_only=True)
#     category_choose = serializers.PrimaryKeyRelatedField(
#         queryset=Category.objects.all(),
#         source="category",
#         write_only=True
#     )

#     subcategory = serializers.StringRelatedField(read_only=True)
#     subcategory_choose = serializers.PrimaryKeyRelatedField(
#         queryset=Subcategory.objects.all(),
#         source="subcategory",
#         write_only=True,
#         required=False
#     )

#     def create(self, validated_data):
#         input_image = validated_data.pop("preview")
#         file = save_image(input_image=input_image, title=validated_data.get('title'))
#         validated_data["preview"] = file

#         return super().create(validated_data)
    
#     def update(self, instance, validated_data):
#         input_image = validated_data.pop("preview", None)
        
#         if input_image is not None:
#             file = save_image(input_image)
#             validated_data.update({ "preview": file })

#         return super().update(instance, validated_data)

#     class Meta:
#         model = Article
#         fields = ["id", "title", "short_title", "category", "subcategory", "desc", "content", "views", "preview", "created_at", "category_choose", "subcategory_choose"]
#         read_only_fields = ["views", "created_at"]


# class AlbumSerializer(serializers.ModelSerializer):
#     category = serializers.StringRelatedField(read_only=True)
#     category_choose = serializers.PrimaryKeyRelatedField(
#         queryset=Category.objects.all(),
#         source="category",
#         write_only=True
#     )
    
#     subcategory = serializers.StringRelatedField(read_only=True)
#     subcategory_choose = serializers.PrimaryKeyRelatedField(
#         queryset=Subcategory.objects.all(),
#         source="subcategory",
#         write_only=True,
#         required=False
#     )

#     def create(self, validated_data):
#         input_image = validated_data.pop("preview")
#         file = save_image(input_image=input_image)
#         validated_data["preview"] = file

#         return super().create(validated_data)
    
#     def update(self, instance, validated_data):
#         input_image = validated_data.pop("preview", None)
        
#         if input_image is not None:
#             file = save_image(input_image)
#             validated_data.update({ "preview": file })

#         return super().update(instance, validated_data)

#     class Meta:
#         model = Album
#         fields = ["id", "title", "short_title", "category", "subcategory", "desc", "content", "views", "preview", "created_at", "category_choose", "subcategory_choose"]
#         read_only_fields = ["views", "created_at"]


class ImageSerializer(serializers.ModelSerializer):
    
    def create(self, validated_data):
        input_image = validated_data.pop("image")
        file = save_image(input_image=input_image)
        validated_data.update({"image": file})

        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        input_image = validated_data.pop("preview", None)
        
        if input_image is not None:
            file = save_image(input_image)
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


# class SearchResultSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     short_title = serializers.CharField()
#     desc = serializers.CharField()
#     content = serializers.CharField()
#     views = serializers.IntegerField()
#     preview = serializers.ImageField()
#     created_at = serializers.DateTimeField()


class ReelSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        input_image = validated_data.pop("image")
        file = save_image(input_image=input_image)
        validated_data.update({"image": file})

        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        input_image = validated_data.pop("image", None)
        
        if input_image is not None:
            file = save_image(input_image)
            validated_data.update({ "image": file })

        return super().update(instance, validated_data)

    class Meta:
        model = Reel
        fields = ["id", "title", "image", "content", "created_at"]
        read_only_fields = ["created_at"]