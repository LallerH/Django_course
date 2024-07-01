from django import forms

class CustomerForm(forms.Form):
    first_name = forms.CharField(max_length=200, required=False)
    last_name = forms.CharField(max_length=200, required=False)
    email = forms.EmailField(max_length=200, required=False, widget=forms.TextInput(attrs={'placeholder':'email address'}))

class ProductForm(forms.Form):
    product_name = forms.CharField(max_length=200, required=False)
