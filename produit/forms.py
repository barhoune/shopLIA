from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.DecimalField()
    date = forms.DateTimeField()
    image=forms.ImageField()