from django import forms
from django.forms import ModelForm
from TP2Q3.models import Car

class BillForm(forms.Form):
    buyerName=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'value':'Enter buyer\'s name'}))
    carId=forms.IntegerField(min_value=1,widget=forms.NumberInput())
    billID=forms.IntegerField(min_value=1, widget=forms.NumberInput())

class AddCarForm(ModelForm):
    class Meta:
        model = Car
        exclude = ['sold']