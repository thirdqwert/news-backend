import io
import pillow_avif
from datetime import datetime
from PIL import Image as Pillow_Image
from django.db.models import Q
from django.core.files.base import ContentFile


def save_image(input_image):
    # Функция конвертирование и сохранение изображений 
    img = Pillow_Image.open(input_image)
    buffer = io.BytesIO()
    img.save(buffer, format="AVIF", quality=50)
    file_name = f"{str(datetime.now())}.avif"
    django_file = ContentFile(buffer.getvalue(), name=file_name)

    return django_file


def save_preview(input_image):
    img = Pillow_Image.open(input_image)

    target_ratio = 1200 / 630
    width, height = img.size
    current_ratio = width / height

    if current_ratio > target_ratio:
        new_width = int(height * target_ratio)
        left = (width - new_width) // 2
        img = img.crop((left, 0, left + new_width, height))
    else:
        new_height = int(width / target_ratio)
        top = (height - new_height) // 2
        img = img.crop((0, top, width, top + new_height))

    img = img.resize((1200, 630), Pillow_Image.LANCZOS)

    buffer = io.BytesIO()
    img.save(buffer, format="AVIF", quality=60)
    file_name = f"preview_{str(datetime.now())}.avif"
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
            queryset = queryset.filter(category__slug=categoryBy)

        if subcategoryBy is not None:
            queryset = queryset.filter(subcategory__slug=subcategoryBy)

        queryset = queryset.order_by(orderBy or '-created_at')

        return queryset
