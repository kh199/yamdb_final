# Generated by Django 2.2.16 on 2022-03-05 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_category_desctiption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='desctiption',
            new_name='description',
        ),
    ]
