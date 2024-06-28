from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    age = models.IntegerField()
    phone_number = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Address(models.Model):
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    zip_code = models.CharField(max_length=200)
    customer = models.OneToOneField(Customer, on_delete=models.PROTECT, related_name='address')

    def __str__(self):
        return f'{self.zip_code}, {self.city}, {self.street}'
    
    class Meta:
        verbose_name = 'Home address'
        verbose_name_plural = 'Addresses'

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.IntegerField()
    is_discounted = models.BooleanField(default=False)
    expiry = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return self.product_name

class Purchase(models.Model):
    purchase_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, related_name='purchases')
    products = models.ManyToManyField(Product, through='PurchaseItem')
    
    def __str__(self):
        return f'{self.id} - {self.purchase_date}'

class PurchaseItem(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    purchase = models.ForeignKey(Purchase, on_delete=models.PROTECT, related_name='items')
    
    def __str__(self):
        return f'{self.quantity} * {self.product}'
