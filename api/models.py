from django.db import models


# тз
# система изображений 
# система рекламы
# система ключа
# сисема rate limit
# система голосовый сообщений
# система конфериацмй изображений в afiv
# система отправки всех фото и статей полностю если надо
# возможно redis 
class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название категории")
    slug = models.SlugField(default='', verbose_name="Slug название")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title
    

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="subcategories", verbose_name="Категория подкатегории")
    title = models.CharField(verbose_name="Название подкатегории")
    slug = models.SlugField(default='', verbose_name="Slug название")
    
    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название новости")
    short_title = models.CharField(max_length=50, verbose_name="Краткое название новости")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория новости")
    subcategory = models.ForeignKey(Subcategory, null=True, blank=True, on_delete=models.PROTECT, verbose_name="Подкатегория новости")
    desc = models.TextField(verbose_name="Ознакомительное описание")
    content = models.TextField(verbose_name="Html код для страницы")
    views = models.IntegerField(default=0, verbose_name="Количество просмотров новости")
    preview = models.ImageField(upload_to="news/", verbose_name="Превью изображение")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


# class Article(models.Model):
#     title = models.CharField(max_length=200, verbose_name="Название статьи")
#     short_title = models.CharField(max_length=50, verbose_name="Краткое название статьи")
#     category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория статьи")
#     subcategory = models.ForeignKey(Subcategory, null=True, blank=True, on_delete=models.PROTECT, verbose_name="Подкатегория новости")
#     desc = models.TextField(verbose_name="Ознакомительное описание")
#     content = models.TextField(verbose_name="Html код для страницы")
#     views = models.IntegerField(default=0, verbose_name="Количество просмотров статьи")
#     preview = models.ImageField(upload_to="articles/", verbose_name="Превью изображение")
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    
#     class Meta:
#         verbose_name = "Статья"
#         verbose_name_plural = "Статьи"


# class Album(models.Model):
#     title = models.CharField(max_length=200, verbose_name="Название альбома")
#     short_title = models.CharField(max_length=50, verbose_name="Краткое название альбома")
#     category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория альбома")
#     subcategory = models.ForeignKey(Subcategory, null=True, blank=True, on_delete=models.PROTECT, verbose_name="Подкатегория новости")
#     desc = models.TextField(verbose_name="Ознакомительное описание")
#     content = models.TextField(verbose_name="Html код для страницы")
#     views = models.IntegerField(default=0, verbose_name="Количество просмотров альбома")
#     preview = models.ImageField(upload_to="album/", verbose_name="Превью изображение")
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")

#     class Meta:
#         verbose_name = "Альбом"
#         verbose_name_plural = "Альбомы"



class Image(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название изображение")
    image = models.ImageField(upload_to="allImages", verbose_name="Изображения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")


    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"
        ordering = ["-created_at"]


class Audio(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название аудио")
    audio = models.FileField(upload_to="allAudio", verbose_name="Аудио")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")

    class Meta:
        verbose_name = "Аудио"
        verbose_name_plural = "Аудио"
        ordering = ["-created_at"]


class Reel(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название рилса")
    image = models.ImageField(upload_to="reels", verbose_name="Превью рилса")
    content = models.TextField(verbose_name="Втройка рилса")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки рилса на сайт")

    class Meta:
        verbose_name = "Рилс"
        verbose_name_plural = "Рилс"