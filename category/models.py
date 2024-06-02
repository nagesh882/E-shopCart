from django.db import models

# I create model class as category name

class Category(models.Model):
    category_id = models.BigAutoField(primary_key=True, unique=True)
    category_name = models.CharField(max_length=100, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    category_image = models.ImageField(upload_to="photos/categories", blank=True)


    def __str__(self):
        return self.category_name