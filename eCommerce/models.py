from django.db import models


class Product(models.Model):
    product_name=models.CharField(max_length=30)
    product_price=models.IntegerField()
    product_description=models.CharField(max_length=50)
    rating=models.FloatField()
    product_img=models.ImageField(upload_to='static/images')
    product_category=models.CharField(max_length=20)
    product_tag=models.CharField(max_length=30)
    product_id=models.IntegerField()

    def __str__(self) -> str:
        return self.product_name + " " + self.product_description
    
# Create your models here.
