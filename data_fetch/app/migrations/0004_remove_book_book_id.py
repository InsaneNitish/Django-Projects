# Generated by Django 4.2.6 on 2023-12-08 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_book_book_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_id',
        ),
    ]