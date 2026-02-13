from django.contrib import admin
from .models import News, Category, Image, Article, Audio, Album


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["pk", "title"]
    list_display_links = ["pk"]
    ordering = ["pk"]
    list_per_page = 36
    search_fields = ["title"]


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "created_at"]
    list_display_links = ["pk"]
    filter_horizontal = ["category"]
    list_filter = ["category"]
    ordering = ["pk"]
    list_per_page = 36
    search_fields = ["title"]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "created_at"]
    list_display_links = ["pk"]
    ordering = ["pk"]
    list_per_page = 36
    search_fields = ["title"]


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "created_at"]
    list_display_links = ["pk"]
    ordering = ["pk"]
    list_per_page = 36
    search_fields = ["title"]



@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "created_at"]
    list_display_links = ["pk"]
    ordering = ["pk"]
    list_per_page = 36
    search_fields = ["title"]



@admin.register(Audio)
class AudioAdmin(admin.ModelAdmin):
    list_display = ["pk", "title", "created_at"]
    list_display_links = ["pk"]
    ordering = ["pk"]
    list_per_page = 36
    search_fields = ["title"]
    