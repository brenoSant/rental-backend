from django_filters import filterset
from core import models


class CategoryFilter(filterset.FilterSet):
    name = filterset.CharFilter(lookup_expr='exact')

    class Meta:
        model = models.Category
        fields = ['name']
