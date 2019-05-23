from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Department

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = get_user_model()
		fields = ('id', 'username', 'email', 'groups', 'bio')


class DepartmentSerializer(serializers.ModelSerializer):

	class Meta:
		model = Department
		fields = ('name', 'over_head_costs')