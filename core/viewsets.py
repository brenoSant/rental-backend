from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from core import filters

from core import models, serializer


class ViewSetBase(ModelViewSet):
    ...
    # permission_classes = (IsAuthenticated,)


class CategoryViewSet(ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializer.CategorySerializer
    filterset_class = filters.CategoryFilter
    ordering_fields = '__all__'
    ordering = ('-id',)


class DvdViewSet(ModelViewSet):
    queryset = models.Dvd.objects.all()
    serializer_class = serializer.DvdSerializer
    ordering = ('-id',)


class RentalItemViewSet(ModelViewSet):
    queryset = models.RentalItem.objects.all()
    serializer_class = serializer.RentalItemSerializer
    ordering = ('-id',)


class RentalViewSet(ModelViewSet):
    queryset = models.Rental.objects.all()
    serializer_class = serializer.RentalSerializer
    ordering = ('-id',)


class EmployeeViewSet(ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializer.EmployeeSerializer
    ordering = ('-id',)


class CustomerViewSet(ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializer.CustomerSerializer
    ordering = ('-id',)
