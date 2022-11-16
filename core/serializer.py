from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from core import models


class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class DvdSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Dvd
        fields = '__all__'
        expandable_fields = {
            'category': (
                CategorySerializer,
                {"fields": ["name"]}
            )
        }


class RentalItemSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.RentalItem
        fields = '__all__'


class RentalSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Rental
        fields = '__all__'


class EmployeeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Employee
        fields = '__all__'


class CustomerSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'
