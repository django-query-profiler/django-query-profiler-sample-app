from django import forms

COFFEE_CHOICES = [
    ('cappuccino', 'Cappuccino'),
    ('latte', 'Latte'),
    ('mocha', 'Mocha'),
]

class OrderForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    coffee_order = forms.ChoiceField(choices=COFFEE_CHOICES, widget=forms.Select())