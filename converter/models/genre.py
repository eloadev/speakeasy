from django.db import models


class Genre(models.Model):
    genre_name = models.CharField(db_column='name', max_length=200, blank=False)

    def __str__(self):
        return self.genre_name
