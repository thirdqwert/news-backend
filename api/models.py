from django.db import models


# тз
# система изображений 
# система рекламы
# система ключа
# система количсетво запросов

class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название новости")
    category = models.ManyToManyField(Category, verbose_name="Категория новости")
    desc = models.TextField(verbose_name="Ознакомительное описание")
    content = models.TextField(verbose_name="Html код для страницы")
    news_views = models.IntegerField(default=0, verbose_name="Количество просмотров новости")
    preview = models.CharField(verbose_name="Превью изображение")
    # нужно решить проьлему с избражения. Где хранить и как хранить
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Image(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название изображение")
    image_link = models.CharField(verbose_name="Ссылка на изображения")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")


    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"