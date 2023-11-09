# Generated by Django 4.2.6 on 2023-11-06 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCommerce', '0005_alter_product_product_img_alter_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]