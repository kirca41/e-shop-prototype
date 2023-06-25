from django import forms
from .models import *


class ProductForm(forms.Form):
    GUITARS = "GUITARS"
    KEYBOARDS = "KEYBOARDS"
    PERCUSSION = "PERCUSSION"
    AMPLIFIERS = "AMPLIFIERS"
    CABLES = "CABLES"
    CATEGORY_CHOICES = [
        (GUITARS, "Guitars"),
        (KEYBOARDS, "Keyboards"),
        (PERCUSSION, "Percussion"),
        (AMPLIFIERS, "Amplifiers"),
        (CABLES, "Cables"),
    ]

    name = forms.CharField(max_length=255)
    model = forms.CharField(max_length=255)
    image_url = forms.URLField()
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    quantity = forms.IntegerField()
    description = forms.CharField(widget=forms.Textarea(attrs={"max_length": 500}))
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, initial=GUITARS)
    manufacturer = forms.ModelChoiceField(queryset=Manufacturer.objects.all(), empty_label='Manufacturer')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Name'
        self.fields['model'].widget.attrs['placeholder'] = 'Model'
        self.fields['image_url'].widget.attrs['placeholder'] = 'Image URL'
        self.fields['price'].widget.attrs['placeholder'] = 'Price'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Quantity'
        self.fields['description'].widget.attrs['placeholder'] = 'Description'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'address', 'city', 'postal_code', 'online_payment']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Surname'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal code'}),
            'online_payment': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }