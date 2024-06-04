from django.contrib import admin
from store.models import Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'product_slug':('product_name',)}
    ordering = ['-product_id']
    list_display = ['product_name', 'price', 'stock', 'category', 'modified_date', "is_availabel"]
    list_display_links = ['product_name', 'category']