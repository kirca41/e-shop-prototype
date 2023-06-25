from django.contrib.auth.models import User
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name} - {self.country}'


class Product(models.Model):
    GUITARS = "GUITARS"
    KEYBOARDS = "KEYBOARDS"
    PERCUSSION = "PERCUSSION"
    AMPLIFIERS = "AMPLIFIERS"
    CABLES = "CABLES"
    CATEGORY_CHOICES = [
        (GUITARS, "Guitars"),
        (KEYBOARDS, "Keyboards"),
        (PERCUSSION, "Percussion"),
        (AMPLIFIERS, "Amplifiers"),
        (CABLES, "Cables"),
    ]
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    image_url = models.URLField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    quantity = models.IntegerField()
    description = models.TextField(max_length=500)
    category = models.CharField(
        max_length=15,
        choices=CATEGORY_CHOICES,
        default=GUITARS,
    )
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.manufacturer.name} {self.name} {self.model}'


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class ProductInShoppingCart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shopping_cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class Order(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    online_payment = models.BooleanField(default=False)


class ProductInOrder(models.Model):
    quantity = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)