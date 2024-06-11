from django.db import models
from store.models import Product, Variation
# Create your models here.



# Cart model created 
class Cart(models.Model):
    cart_id = models.CharField(max_length=255, default=None, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cart_id
    


# Cart Model created 
class CartItem(models.Model):
    cart_item_id = models.BigAutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    variations = models.ManyToManyField(Variation, blank=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product}"
    
    def sub_total(self):
        return self.product.price * self.quantity
