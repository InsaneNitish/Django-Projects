from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    product_name=models.CharField(max_length=30)
    product_price=models.IntegerField()
    product_description=models.TextField(blank=True)
    rating=models.FloatField()
    product_img=models.ImageField(upload_to='product_images/',blank=True,null=True)
    product_category=models.TextField(max_length=20)
    product_tag=models.CharField(max_length=50)
    product_id=models.IntegerField()

    def __str__(self) -> str:
        return self.product_name + " " + self.product_description
    


# Create your models here.
