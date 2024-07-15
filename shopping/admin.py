from django.contrib import admin

# Register your models here.

from .models import Customer, Product, Purchase, Address, PurchaseItem
from .filters import AgeRangeFilter
from .filters2 import PriceRangeFilter, QuantityRangeFilter

class PurchaseItemInline(admin.TabularInline):
    model = PurchaseItem
    extra = 0

class PurchaseInline(admin.TabularInline):
    model = Purchase
    extra = 0

class AddressInline(admin.TabularInline):
    model = Address
    extra = 0

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'age')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = (AgeRangeFilter,)
    ordering = ('first_name','last_name', 'age')
    readonly_fields = ('email',)
    inlines = [PurchaseInline, AddressInline]


def set_discounted(modeladmin, request, queryset):
    count = queryset.update(is_discounted=True)
    modeladmin.message_user(request, f'Updated products: {count}')

set_discounted.short_description = 'Set selected products as discounted'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price', 'is_discounted', 'storage_quantity')
    actions = [set_discounted]
    actions_on_top = True
    actions_on_bottom = False
    list_filter = (PriceRangeFilter,QuantityRangeFilter)

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('purchase_date',)
    inlines = [PurchaseItemInline]
    raw_id_fields = ('customer',)


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Address)
admin.site.register(PurchaseItem)

