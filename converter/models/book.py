from django.db import models
from .genre import Genre
from .s3mediastorage import S3MediaStorage
from .audiobook import AudioBook


class Book(models.Model):
    book_title = models.CharField(db_column='title', max_length=200, blank=False)
    book_description = models.TextField(db_column='description', blank=False)
    book_author = models.CharField(db_column='author', max_length=200, blank=False)
    book_year = models.IntegerField(db_column='year', blank=False)
    audio_book = models.OneToOneField(AudioBook, related_name='audio_book',
                                      on_delete=models.CASCADE, null=True)
    book_genres = models.ManyToManyField(Genre, related_name='book_genres', blank=False)
    book_file = models.FileField(upload_to='books/', storage=S3MediaStorage(), null=False, blank=False)

    def delete(self, *args, **kwargs):
        if self.audio_book:
            self.audio_book.delete()

        if self.book_file:
            self.book_file.storage.delete(self.book_file.name)

        super().delete(*args, **kwargs)

    def __str__(self):
        return self.book_title
