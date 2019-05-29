from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .models import Department, Product

# HyperlinkedModelSerializer has field 'url'


class UserSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.ReadOnlyField()
	
	class Meta:
		model = get_user_model()
		fields = ('url', 'id', 'username', 'email', 'groups', 'bio')  # select only certain fields


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.ReadOnlyField()

	class Meta:
		model = Group
		fields = ('url', 'id', 'name')

class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.ReadOnlyField()
	products = serializers.HyperlinkedRelatedField(view_name='product-detail', many=True, queryset=Product.objects.all())  # allows lookup of all product ids for each department
	created_by = serializers.ReadOnlyField(source="created_by.username")  # Changes which attribute is used to populate a field

	class Meta:
		model = Department
		fields = '__all__'  # shorthand for all fields


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	id = serializers.ReadOnlyField()
	department_name = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), source='department', allow_null=False, required=True)

	class Meta:
		model = Product
		fields = ('id', 'url', 'name', 'department_name', 'price', 'stock_quantity', 'product_sales')
		
	def validate(self, data):
		if data['price'] < 0 or data['stock_quantity'] < 0 or data['product_sales'] < 0:
			raise serializers.ValidationError('Price, stock quantity, and product sale numbers must all be >= 0.')
		return data


class ValidateIntegerSerializer(serializers.Serializer):
	"""Validates that object value at 'stock_to_purchase' is an integer."""
	stock_to_purchase = serializers.IntegerField()

	def validate(self, data):
		try:
			return int(data['stock_to_purchase'])
		except (ValueError, TypeError):
			raise serializers.ValidationError('stock quantity must be an integer >= 0.')


# class UserSerializer(serializers.ModelSerializer):

# 	class Meta:
# 		model = get_user_model()
# 		fields = ('id', 'username', 'email', 'groups', 'bio')  # select only certain fields


# class DepartmentSerializer(serializers.ModelSerializer):
# 	products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())  # allows lookup of all product ids for each department
# 	created_by = serializers.ReadOnlyField(source="created_by.username")  # Changes which attribute is used to populate a field

# 	class Meta:
# 		model = Department
# 		fields = '__all__'  # shorthand for all fields


# class ProductSerializer(serializers.ModelSerializer):
# 	department = serializers.ReadOnlyField(source="department.name")

# 	class Meta:
# 		model = Product
# 		fields = '__all__'
		