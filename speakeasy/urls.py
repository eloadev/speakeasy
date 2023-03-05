from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from converter import views

urlpatterns = [
    path('', views.index, name="index"),
    path('book/create', views.book_create, name="book_create"),
    path('genre/create', views.genre_create, name="genre_create"),
    path('book/retrieve/<int:book_id>', views.book_retrieve, name='book_retrieve'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
