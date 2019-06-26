from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_subs = models.BooleanField(default=False)


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Статья')
    image = models.ImageField(upload_to='static/img', verbose_name='Изображение')
    paid_article = models.BooleanField(default=False)