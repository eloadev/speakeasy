from django.db import models
from .s3mediastorage import S3MediaStorage


class AudioBook(models.Model):
    audio_book_file = models.FileField(upload_to='audiobooks/', storage=S3MediaStorage())

    def delete(self, *args, **kwargs):
        self.audio_book_file.storage.delete(self.audio_book_file.name)
        super().delete(*args, **kwargs)
