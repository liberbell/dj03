from django import forms

class PizzaForm(forms.Form):
    topping1 = forms.CharField(label='Topping 1', max_length=100)
