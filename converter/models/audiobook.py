from django.db import models
from .s3mediastorage import S3MediaStorage

class AudioBook(models.Model):
    audio_book_file = models.FileField(upload_to='audiobooks/', storage=S3MediaStorage(), null=False, blank=False)