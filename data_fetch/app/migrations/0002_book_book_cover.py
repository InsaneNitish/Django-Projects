# Generated by Django 4.2.6 on 2023-12-08 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(blank=True, null=True, upload_to='book_images/'),
        ),
    ]