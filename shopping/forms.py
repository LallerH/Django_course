from django import forms
from .models import Customer

class CustomerForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=False)
    last_name = forms.CharField(max_length=200, required=False)
    email = forms.EmailField(max_length=200, required=False, widget=forms.TextInput(attrs={'placeholder':'email address'}))

# class CustomerRegisterForm(forms.Form):
#     first_name = forms.CharField(max_length=200)
#     last_name = forms.CharField(max_length=200)
#     email = forms.EmailField(max_length=200)
#     age = forms.IntegerField()
#     phone_number = forms.CharField(max_length=200, required=False)

class CustomerRegisterForm(forms.ModelForm):
    class Meta:
        model = Customer
        # fields = ['first_name', 'last_name']
        fields = '__all__'
        # exclude = ['phone_number']

class ProductForm(forms.Form):
    product_name = forms.CharField(max_length=200, required=False)
