from django import forms

COFFEE_CHOICES = [
    ('americano', 'Americano'),
    ('cappuccino', 'Cappuccino'),
    ('glace', 'Glace'),
    ('mocha', 'Mocha'),
    ('hot_chocolate', 'Hot Chocolate'),
    ('irish', 'Irish'),
    ('latte', 'Latte'),
    ('espresso', 'Espresso'),
    ('macchiato', 'Macchiato'),
]

class OrderForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    coffee_order = forms.ChoiceField(choices=COFFEE_CHOICES, widget=forms.Select())