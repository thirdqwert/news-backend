from rest_framework.routers import DefaultRouter
from .swagger_settings import urlpatterns as urls_swagger
from . import views
from django.urls import path


router = DefaultRouter()
router.register("news", viewset=views.NewsViewSet, basename="news")
router.register("images", viewset=views.ImageViewSet, basename="images")
router.register("articles", viewset=views.ArticleViewSet, basename="article")
router.register("audios", viewset=views.AudioViewSet, basename="audios")
router.register("albums", viewset=views.AlbumViewSet, basename="albums")

patterns = [
    path("categories/", views.CategoryList.as_view(), name="categories_list"),
    path("categories/create", views.CategoryCreate.as_view(), name="categories_create"),
]

urlpatterns = patterns + router.urls + urls_swagger