# users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Department, Product


@admin.register(User)  # Register model shortcut
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'bio']


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'over_head_costs']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'price', 'stock_quantity', 'product_sales']
