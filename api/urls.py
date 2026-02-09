from rest_framework.routers import DefaultRouter
from .swagger_settings import urlpatterns as urls_swagger
from . import views
from django.urls import path


router = DefaultRouter()
router.register('news', viewset=views.NewsViewSet, basename='news')
router.register('images', viewset=views.ImageViewSet, basename='images')

patterns = [
    path('categories/', views.CategoryList.as_view(), name='categories_list'),

]

urlpatterns = patterns + router.urls + urls_swagger