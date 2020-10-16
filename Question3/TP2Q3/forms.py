from django import forms

class BillForm(forms.Form):
    buyerName=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'value':'Enter buyer\'s name'}))
    carId=forms.IntegerField(min_value=1,widget=forms.NumberInput())

