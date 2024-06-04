from django.contrib import admin
from category.models import Category
# Register your models here.




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"category_slug":("category_name",)}
    ordering = ["-category_id"]
    list_display = ["category_name", "category_slug"]
    list_display_links = ["category_name", "category_slug"]

