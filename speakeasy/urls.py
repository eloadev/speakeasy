from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from converter.views import book, genre, index
from converter.views.user import create_user, CustomSignupView, CustomLoginView

urlpatterns = [
    path('', index.index, name="index"),
    #path('book/create', book.book_create, name="book_create"),
    #path('book/delete/<int:book_id>', book.book_delete, name='book_delete'),
    #path('book/retrieve/<int:book_id>', book.book_retrieve, name='book_retrieve'),
    #path('genre/create', genre.genre_create, name="genre_create"),
    path('account/', include('allauth.urls')),
    path('create-user/', create_user, name='create_user'),
    path('account/signup/', CustomSignupView.as_view(), name='account_signup'),
    path('account/login/', CustomLoginView.as_view(), name='account_login'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
