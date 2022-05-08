from dataclasses import fields
from django import forms
from .models import Product

class ImageForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = ("product_name", "product_description", "product_price", "product_img", "category", "slug")