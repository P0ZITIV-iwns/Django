from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name="Автор")
    body = models.TextField(verbose_name="Текст")
    email = models.EmailField(blank=True, verbose_name="Эл. адрес")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])