from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from converter.views import book, genre, index

urlpatterns = [
    path('', index.index, name="index"),
    path('book/create', book.book_create, name="book_create"),
    path('genre/create', genre.genre_create, name="genre_create"),
    path('book/retrieve/<int:book_id>', book.book_retrieve, name='book_retrieve'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
