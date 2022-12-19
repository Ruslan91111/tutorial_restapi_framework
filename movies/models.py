from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название фильма")


    def __str__(self):
        return self.title

    class Meta:
        app_label = 'movies'


