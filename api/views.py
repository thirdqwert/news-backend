from rest_framework import viewsets, generics, permissions, pagination, response
from django.db.models import Q
from .models import Category, News, Image, Article, Audio, Album
from .serializers import NewsSerializer, CategorySerializer, ImageSerializer, Article, ArticleSerializer, AudioSerializer, AlbumSerializer, SearchResultSerializer
from .utils import filter_data

class Pagination(pagination.PageNumberPagination):
    page_size = 12


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = Pagination

    def get_queryset(self):
        return filter_data(self.request, News.objects.all())

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super().get_permissions()
    
    def paginate_queryset(self, queryset):
        user = self.request.user

        # если запрос делат админ то вренуть весь список без пагинации
        if user.is_staff or user.is_superuser:
            return None
        
        return super().paginate_queryset(queryset)


    def retrieve(self, request, *args, **kwargs):
        news = self.get_object()
        news.views = news.views + 1
        news.save()
        serializer = self.get_serializer(news)
        return response.Response(serializer.data)
    
    
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer


class CategoryCreate(generics.CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser]



class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = Pagination


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = Pagination

    def get_queryset(self):
        return filter_data(self.request, Article.objects.all())

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super().get_permissions()
    
    def paginate_queryset(self, queryset):
        user = self.request.user

        # если запрос делат админ то вренуть весь список без пагинации
        if user.is_staff or user.is_superuser:
            return None
        return super().paginate_queryset(queryset)

    def retrieve(self, request, *args, **kwargs):
        news = self.get_object()
        news.views = news.views + 1
        news.save()
        serializer = self.get_serializer(news)
        return response.Response(serializer.data)
    
    
class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = Pagination

    def get_queryset(self):
        return filter_data(self.request, Album.objects.all())

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super().get_permissions()

    def paginate_queryset(self, queryset):
        user = self.request.user

        # если запрос делат админ то вренуть весь список без пагинации
        if user.is_staff or user.is_superuser:
            return None
        return super().paginate_queryset(queryset)
    
    def retrieve(self, request, *args, **kwargs):
        news = self.get_object()
        news.views = news.views + 1
        news.save()
        serializer = self.get_serializer(news)
        return response.Response(serializer.data)


class AudioViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = Pagination


class SearchList(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SearchResultSerializer
    pagination_class = Pagination
    
    def get_queryset(self):
        fields = ["title", "short_title", "desc", "content", "views","preview", "created_at"]
        searchBy = self.request.query_params.get("searchBy", "")
        news_queryset = News.objects.filter(Q(title__icontains=searchBy) | Q(desc__icontains=searchBy)).values(*fields)
        article_queryset = Article.objects.filter(Q(title__icontains=searchBy) | Q(desc__icontains=searchBy)).values(*fields)
        album_queryset = Album.objects.filter(Q(title__icontains=searchBy) | Q(desc__icontains=searchBy)).values(*fields)
        queryset = news_queryset.union(article_queryset, album_queryset)
        queryset.order_by("-created_at")
        print(queryset)
        return queryset