# Generated by Django 2.2 on 2019-06-26 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20190626_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
    ]