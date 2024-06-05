from django.db import models
from django.urls import reverse

# I create model class as category name

class Category(models.Model):
    category_id = models.BigAutoField(primary_key=True, unique=True)
    category_name = models.CharField(max_length=100, unique=True)
    category_slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    category_image = models.ImageField(upload_to="photos/categories", blank=True)


    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        

    def get_url(self):
        return reverse('products_by_category', args=[self.category_slug])

    def __str__(self):
        return self.category_name