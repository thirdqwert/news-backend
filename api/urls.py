from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
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
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("categories/", views.CategoryList.as_view(), name="categories_list"),
    path("subcategories/", views.SubcategoryList.as_view(), name="subcategories_list"),
    path("search/", views.SearchList.as_view(), name="search_list")
]

urlpatterns = patterns + router.urls + urls_swagger