from django.db import models
from category.models import Category

# I create model class as Product name


class Product(models.Model):
    product_id = models.BigAutoField(primary_key=True, unique=True)
    product_name = models.CharField(max_length=100, unique=True)
    product_slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    product_image = models.ImageField(upload_to="photos/products", blank=True)
    stock = models.IntegerField()
    is_availabel = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    
    def __str__(self):
        return self.product_name