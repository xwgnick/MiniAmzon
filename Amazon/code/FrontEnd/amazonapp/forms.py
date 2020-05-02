from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import AUser, Cart

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = AUser
        fields = ('username', 'email', 'ups_name', 'location_x', 'location_y')

class SearchItem(forms.Form):
    item_name = forms.CharField(max_length=100)

    def clean_item_name(self):
        data = self.cleaned_data['item_name']
        data = data.lower()
        return data

class AddItemToCart(forms.Form):
    quantity = forms.IntegerField(min_value=1)
    
    def clean_quantity(self):
        data = self.cleaned_data['quantity']
        return data

class DeliverInfo(forms.Form):
    location_x = forms.IntegerField()
    location_y = forms.IntegerField()
    ups_username = forms.CharField(max_length=100)

    def clean_location_x(self):
        data = self.cleaned_data["location_x"]
        return data
    def clean_location_y(self):
        data = self.cleaned_data["location_y"]
        return data
    def clean_ups_username(self):
        data = self.cleaned_data["ups_username"]
        return data

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ['count']
 