from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name','item_desc','item_image','item_opening_hours','item_shipping','item_shipping_available','item_sales','item_allowed_people','item_people_inside']

