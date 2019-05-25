from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Department, Product

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = get_user_model()
		fields = ('id', 'username', 'email', 'groups', 'bio')


class DepartmentSerializer(serializers.ModelSerializer):
	products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
	created_by = serializers.ReadOnlyField(source="created_by.username")

	class Meta:
		model = Department
		fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

	class Meta:
		model = Product
		# fields = ('name', 'department', 'price', 'stock_quantity', 'product_sales')
		fields = '__all__'

		
		