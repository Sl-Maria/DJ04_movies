from django.db import models

class Films(models.Model):
    title = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')
    review = models.TextField('Отзыв')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'