# Generated by Django 2.2.16 on 2022-03-09 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0017_auto_20220309_2051'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'ordering': ['pub_date'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['pub_date'], 'verbose_name': 'Обзор', 'verbose_name_plural': 'Обзоры'},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ['name'], 'verbose_name': 'Произведение', 'verbose_name_plural': 'Произведения'},
        ),
    ]