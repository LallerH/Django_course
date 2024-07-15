from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet

class PriceRangeFilter(admin.SimpleListFilter):
    title = 'Price range'
    parameter_name = 'price_range'

    def lookups(self, request, model_admin):
        return [
            ('0', '<100'),
            ('1', '100-200'),
            ('2', '201-300'),
            ('3', '301-400'),
            ('4', '400<'),
        ]
    
    def queryset(self, request, queryset):
        if self.value() == '0':
            queryset = queryset.filter(product_price__lt=100)
        if self.value() == '1':
            queryset = queryset.filter(product_price__gte=100, product_price__lte=200)
        if self.value() == '2':
            queryset = queryset.filter(product_price__gte=201, product_price__lte=300)
        if self.value() == '3':
            queryset = queryset.filter(product_price__gte=301, product_price__lte=400)
        if self.value() == '4':
            queryset = queryset.filter(product_price__gte=401)
        
        return queryset


class AgeRangeFilter(admin.SimpleListFilter):
    title = 'Age range'
    parameter_name = 'age_range'

    def lookups(self, request, model_admin):
        return [
            ('0', '<10'),
            ('1', '10-20'),
            ('2', '21-30'),
            ('3', '31-40'),
            ('4', '40<'),
        ]
    
    def queryset(self, request, queryset):
        if self.value() == '0':
            queryset = queryset.filter(age__lt=10)
        if self.value() == '1':
            queryset = queryset.filter(age__gte=10, age__lte=20)
        if self.value() == '2':
            queryset = queryset.filter(age__gte=21, age__lte=30)
        if self.value() == '3':
            queryset = queryset.filter(age__gte=31, age__lte=40)
        if self.value() == '4':
            queryset = queryset.filter(age__gte=41)
        
        return queryset
