from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Department, Product

# HyperlinkedModelSerializer user field 'url'


class UserSerializer(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = get_user_model()
		fields = ('url', 'id', 'username', 'email', 'groups', 'bio')  # select only certain fields


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
	products = serializers.HyperlinkedRelatedField(view_name='product-detail', many=True, queryset=Product.objects.all())  # allows lookup of all product ids for each department
	created_by = serializers.ReadOnlyField(source="created_by.username")  # Changes which attribute is used to populate a field

	class Meta:
		model = Department
		fields = '__all__'  # shorthand for all fields


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	department = serializers.ReadOnlyField(source="department.name")

	class Meta:
		model = Product
		fields = '__all__'
		


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
		