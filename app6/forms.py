
from django import forms
from app6.models import Product

class ProductForm(forms.ModelForm):

    quantity = forms.IntegerField(min_value=1)

    class Meta:
        model = Product
        fields = "__all__"

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price >= 1000:
            return price
        else:
            raise forms.ValidationError("Invalid Price")



