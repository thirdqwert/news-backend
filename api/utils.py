import io
import pillow_avif
from datetime import datetime
from PIL import Image as Pillow_Image
from django.db.models import Q
from django.core.files.base import ContentFile


def save_image(input_image, title):
    # Функция конвертирование и сохранение изображений 
    img = Pillow_Image.open(input_image)
    buffer = io.BytesIO()
    img.save(buffer, format="AVIF", quality=60)
    file_name = f"{title + str(datetime.now())}.avif"
    django_file = ContentFile(buffer.getvalue(), name=file_name)

    return django_file


def filter_data(request, queryset):
        orderBy = request.query_params.get('orderBy')
        categoryBy = request.query_params.get('categoryBy')
        subcategoryBy = request.query_params.get('subcategoryBy')
        searchBy = request.query_params.get('searchBy')

        if searchBy is not None:
            queryset = queryset.filter(Q(title__icontains=searchBy) | Q(desc__icontains=searchBy))

        if categoryBy is not None:
            queryset = queryset.filter(category__title=categoryBy)

        if subcategoryBy is not None:
            queryset = queryset.filter(subcategory__title=subcategoryBy)

        queryset = queryset.order_by(orderBy or '-created_at')

        return queryset
