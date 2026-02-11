from rest_framework import viewsets, generics, permissions, pagination, response
from .models import Category, News, Image, Article
from .serializers import NewsSerializer, CategorySerializer, ImageSerializer, Article, ArticleSerializer


class Pagination(pagination.PageNumberPagination):
    page_size = 36


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = Pagination

    def get_queryset(self):
        orderBy = self.request.query_params.get('orderBy')
        queryset = News.objects.all()
        if orderBy is not None:
            queryset = News.objects.all().order_by(orderBy)
        return queryset

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super().get_permissions()

    def retrieve(self, request, *args, **kwargs):
        news = self.get_object()
        news.news_views = news.news_views + 1
        news.save()
        serializer = self.get_serializer(news)
        return response.Response(serializer.data)
    
    
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ImageViewSet(viewsets.ModelViewSet):
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = Pagination

    def get_queryset(self):
        orderBy = self.request.query_params.get('orderBy')
        queryset = Image.objects.all()
        if orderBy is not None:
            queryset = Image.objects.all().order_by(orderBy)
        return queryset


class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAdminUser]
    pagination_class = Pagination

    def get_queryset(self):
        orderBy = self.request.query_params.get('orderBy')
        queryset = Article.objects.all()
        if orderBy is not None:
            queryset = Article.objects.all().order_by(orderBy)
        return queryset

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return super().get_permissions()

    def retrieve(self, request, *args, **kwargs):
        news = self.get_object()
        news.article_views = news.article_views + 1
        news.save()
        serializer = self.get_serializer(news)
        return response.Response(serializer.data)
    
    