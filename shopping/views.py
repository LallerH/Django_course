from django.shortcuts import render, redirect
from .models import Customer, Product
from django.template import loader

# Create your views here.

from django.http import HttpResponse
from .forms import CustomerForm, ProductForm, CustomerRegisterForm

def index(request):
    return render(request,'shopping/index.html')

def get_customers(request):
    customers = Customer.objects.all()
    form = CustomerForm(request.GET or None) # azért kell a NONE, hogyha nincs üres szűrő akkor is működjön
    if form.is_valid():
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')

        customers = Customer.objects.filter(
            first_name__icontains=first_name, last_name__icontains=last_name
            )
    
        if email:
            customers=customers.filter(email=email)

    context = {
        "customers": customers,
        "form": form,
    }
    return render(request,'shopping/customers.html', context)
    
def get_products(request):
    products = Product.objects.all()
    
    form = ProductForm(request.GET or None)
    if form.is_valid():
        product_name = form.cleaned_data.get('product_name')

        products = products.filter(
            product_name__icontains=product_name
            )

    context = {
        "products": products,
        "form": form,
        "title": 'List of products'
    }
    return render(request,'shopping/products.html', context)

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

def add_customer(request):
    if request.POST:
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            #customer = Customer.objects.create(**form.cleaned_data)
            form.save()
            context = {
                "form": CustomerRegisterForm(),
                "success": True
            }
            # return render(request, 'shopping/customer_add.html', context)
            return redirect('customers')
    else:
        form = CustomerRegisterForm()
    
        context = {
            "form": form
        }
        return render(request,'shopping/customer_add.html', context)
  

