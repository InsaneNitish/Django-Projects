# Generated by Django 4.2.6 on 2023-11-28 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eCommerce', '0008_alter_product_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_tag',
            field=models.CharField(max_length=50),
        ),
    ]