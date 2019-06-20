from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from .models import Department, Product

# HyperlinkedModelSerializer creates field 'url'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    password = serializers.CharField(write_only=True)
    bio = serializers.CharField(read_only=True)
    groups = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = get_user_model()
        fields = ('url', 'id', 'username', 'email', 'groups',
                  'bio', 'password')  # select only certain fields


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Group
        fields = ('url', 'id', 'name')


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    # allows lookup of all product ids for each department # TODO fix this lookup
    # products = serializers.HyperlinkedModelSerializer(
        # view_name='product-detail', 
        # source='product', many=True, 
        # queryset=Product.objects.all(), 
        # allow_null=False, required=True)

    # Changes which attribute is used to populate a field
    created_by = serializers.ReadOnlyField(source="created_by.username")

    class Meta:
        model = Department
        fields = '__all__'  # shorthand for all fields


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    department_name = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(), source='department', allow_null=False, required=True)

    class Meta:
        model = Product
        fields = ('id', 'url', 'name', 'department_name',
                  'price', 'stock_quantity', 'product_sales')

    def validate(self, data):
        if data['price'] < 0 or data['stock_quantity'] < 0 or data['product_sales'] < 0:
            raise serializers.ValidationError(
                'price, stock_quantity, and product_sales must all be numbers >= 0.')
        return data


class ValidatePurchaseSerializer(serializers.Serializer):
    """Validates object value at 'stock_to_purchase' is an integer."""
    stock_to_purchase = serializers.IntegerField()

    def validate_stock_to_purchase(self, data):
        if data >= 0:
            return data
        else:
            raise serializers.ValidationError(
                'stock_to_purchase must be an integer >= 0.')


class ValidateAddStockSerializer(serializers.Serializer):
    """Validates object value at 'stock_to_purchase' is an integer."""
    stock_to_add = serializers.IntegerField()

    def validate_stock_to_add(self, data):
        if data >= 0:
            return data
        else:
            raise serializers.ValidationError(
                'stock_to_add must be an integer >= 0.')


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
