from django.contrib import admin

# Register your models here.

from .models import Customer, Product, Purchase, Address, PurchaseItem

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
    list_filter = ('age',)
    ordering = ('first_name','last_name', 'age')
    readonly_fields = ('email',)
    inlines = [PurchaseInline, AddressInline]

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'product_price')

class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('purchase_date',)
    inlines = [PurchaseItemInline]


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Purchase, PurchaseAdmin)
admin.site.register(Address)
admin.site.register(PurchaseItem)

