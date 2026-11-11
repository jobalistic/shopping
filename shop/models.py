from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ("stationery", "stationery"),
    ("electronics", "electronics"),
    ("food", "food"),
    )

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    address = models.CharField(max_length = 128)
    phone = models.CharField(max_length = 128)
    picture = models.ImageField()

    def __str__(self):
        return self.user.username

class Product(models.Model):
    name = models.CharField(max_length = 128)
    category = models.CharField(max_length = 20, choices = CATEGORY,null = True)
    quantity = models.PositiveIntegerField(null = True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete = models.CASCADE, null = True)
    created_by = models.ForeignKey(User, on_delete = models.CASCADE)
    order_quantity = models.PositiveIntegerField(null = True)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.product} order_quantity {self.order_quantity}"



    
