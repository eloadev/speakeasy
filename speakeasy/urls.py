from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from converter.views import index, book_create, genre_create

urlpatterns = [
    path('', index, name="index"),
    path('book/create', book_create, name="book_create"),
    path('genre/create', genre_create, name="genre_create"),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
