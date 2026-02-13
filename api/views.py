from rest_framework import viewsets, generics, permissions, pagination, response
from .models import Category, News, Image, Article, Audio, Album
from .serializers import NewsSerializer, CategorySerializer, ImageSerializer, Article, ArticleSerializer, AudioSerializer, AlbumSerializer


class Pagination(pagination.PageNumberPagination):
    page_size = 36


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = Pagination

    def get_queryset(self):
        orderBy = self.request.query_params.get('orderBy')
        categoriesBy = self.request.query_params.get('categoryBy')
        queryset = News.objects.all()

        if categoriesBy is not None:
            categoriesBy = categoriesBy.split('&')
            for category in categoriesBy:
                queryset = queryset.filter(category__title=category)

        queryset = queryset.order_by(orderBy or '-created_at')

        return queryset

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
        news.news_views = news.news_views + 1
        news.save()
        serializer = self.get_serializer(news)
        return response.Response(serializer.data)
    
    
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
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
        orderBy = self.request.query_params.get('orderBy')
        categoriesBy = self.request.query_params.get('categoryBy')
        queryset = Article.objects.all()

        if categoriesBy is not None:
            categoriesBy = categoriesBy.split('&')
            for category in categoriesBy:
                queryset = queryset.filter(category__title=category)

        queryset = queryset.order_by(orderBy or '-created_at')

        return queryset

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
        news.article_views = news.article_views + 1
        news.save()
        serializer = self.get_serializer(news)
        return response.Response(serializer.data)
    
    
class AlbumViewSet(viewsets.ModelViewSet):
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = Pagination

    def get_queryset(self):
        orderBy = self.request.query_params.get('orderBy')
        categoriesBy = self.request.query_params.get('categoryBy')
        queryset = Album.objects.all()

        if categoriesBy is not None:
            categoriesBy = categoriesBy.split('&')
            for category in categoriesBy:
                queryset = queryset.filter(category__title=category)

        queryset = queryset.order_by(orderBy or '-created_at')

        return queryset

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
        news.article_views = news.article_views + 1
        news.save()
        serializer = self.get_serializer(news)
        return response.Response(serializer.data)


class AudioViewSet(viewsets.ModelViewSet):
    queryset = Audio.objects.all()
    serializer_class = AudioSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = Pagination
