from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    bio = models.TextField(help_text="Enter a bio.", default="")


class Department(models.Model):
    name = models.CharField(unique=True, max_length=100)
    over_head_costs = models.DecimalField(max_digits=10, decimal_places=2)


class Products(models.Model):
    name = models.CharField(unique=True, max_length=100)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    product_sales = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
