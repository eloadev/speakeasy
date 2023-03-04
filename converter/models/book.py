from django.db import models
from .genre import Genre

import boto3
from storages.backends.s3boto3 import S3Boto3Storage


class S3MediaStorage(S3Boto3Storage):
    location = 'books'


class Book(models.Model):
    book_title = models.CharField(db_column='title', max_length=200, blank=False)
    book_description = models.TextField(db_column='description', blank=False)
    book_author = models.CharField(db_column='author', max_length=200, blank=False)
    book_year = models.IntegerField(db_column='year', blank=False)
    book_genres = models.ManyToManyField(Genre, related_name='genre_books', blank=False)
    book_file = models.FileField(upload_to='books/', storage=S3MediaStorage(), null=False, blank=False)

    def __str__(self):
        return self.book_title

    def retrieve_book(self):
        s3 = boto3.client("s3")

        s3.download_file(
            Bucket="speak-easy-bucket", Key=f"books/{self.book_file.name}", Filename="data/downloaded_from_s3.csv"
        )
