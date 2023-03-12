from django.contrib.auth.models import Group
from django import forms
#from django.core import validators
from django.forms import ModelForm

from .models import Product, Order


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['name']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'discount']

class OrderForm(forms.ModelForm):
     class Meta:
         model = Order
         #fields = ['name', 'email', 'phone', 'address']
         fields = ['user', 'products', 'promocode', 'delivery_address']






# class ProductForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     price = forms.DecimalField(min_value=1, max_value=100000, decimal_places=2)
#     description = forms.CharField(
#         label='Product description',
#         widget=forms.Textarea(attrs={'rows': 5, "cols": 100}),
#         validators=[validators.RegexValidator(
#             regex=r"great",
#             message="Description must be great"
#         )]
#     )