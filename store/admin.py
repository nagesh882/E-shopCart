from django.contrib import admin
from store.models import Product, Variation

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'product_slug':('product_name',)}
    ordering = ['-product_id']
    list_display = ['product_name', 'price', 'stock', 'category', 'modified_date', "is_availabel"]
    list_display_links = ['product_name', 'category']



# admin.site.register(Variation)
@admin.register(Variation)
class VariationAdmin(admin.ModelAdmin):
    list_display = ["product", "variation_category", "variation_value", "is_active"]
    list_editable = ("is_active",)
    list_filter = ("product", "variation_category", "variation_value")