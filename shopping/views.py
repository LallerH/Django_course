from django.shortcuts import render
from .models import Customer, Product
from django.template import loader

# Create your views here.

from django.http import HttpResponse
from .forms import CustomerForm

def index(request):
    return HttpResponse('Hello!')

def get_customers(request):
    customers = Customer.objects.all()
    form = CustomerForm(request.GET)
    if form.is_valid():
        first_name = form.data.get('first_name')
        last_name = form.data.get('last_name')
        
        customers = Customer.objects.filter(
            first_name__icontains=first_name, last_name__icontains=last_name
            )
    
    context = {
        "customers": customers,
        "form": form,
    }
    return render(request,'shopping/customers.html', context)
    
def get_products(request):
    products = Product.objects.all()
    
    template = loader.get_template("shopping/products.html")
    context = {
        "products": products,
    }
    return HttpResponse(template.render(context, request))

def get_customer_details(request, customer_id):
    try:
        customer = Customer.objects.get(id=customer_id)
    except Customer.DoesNotExist:
        return HttpResponse('Customer not found!', status=404)

    context = {
        "customer": customer,
    }
    return render(request,'shopping/customer_details.html', context)

def get_product_details(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return HttpResponse('Product not found!', status=404)

    context = {
        "product": product,
    }
    return render(request,'shopping/product_details.html', context)

    

