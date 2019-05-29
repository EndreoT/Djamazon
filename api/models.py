from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    bio = models.TextField(help_text="Enter a bio.", default="")


class Department(models.Model):
    name = models.CharField(unique=True, max_length=100)
    created_by = models.ForeignKey(User, related_name='departments', on_delete=models.SET_NULL, null=True)
    over_head_costs = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    name = models.CharField(unique=True, max_length=100)
    department = models.ForeignKey(Department, related_name='products', on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    product_sales = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def purchaseStock(self, numUnits: int) -> float:
        if self.stock_quantity - numUnits < 0:
            return -1
        cost: float = numUnits * self.price
        self.stock_quantity -= numUnits
        self.product_sales += cost
        self.save()
        return cost

    def increaseStock(self, numUnits: int) -> None:
        self.stock_quantity += numUnits
        self.save()

    def __str__(self):
        return str(self.name)


class PurchaseRecord(models.Model):
    pass
