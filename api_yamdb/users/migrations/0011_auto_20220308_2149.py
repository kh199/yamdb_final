# Generated by Django 2.2.16 on 2022-03-08 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20220308_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('anon', 'anonimous'), ('admin', 'admin'), ('moderator', 'moderator'), ('user', 'user')], default='user', max_length=10, verbose_name='Роль'),
        ),
    ]