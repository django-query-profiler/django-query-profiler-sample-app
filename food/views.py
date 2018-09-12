from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .forms import OrderForm
from .models import OrderInstance

@login_required
@permission_required('food.can_order', raise_exception=True)
def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            coffee_order = form.cleaned_data['coffee_order']
            customer_order = OrderInstance(name=name, email=email, coffee_order=coffee_order)
            customer_order.save()
            return redirect('food:home')
    else:
        form = OrderForm()
    return render(request, "food/order.html", { 'form':form })

def homepage(request):
    return render(request, "food/homepage.html")

@login_required
@permission_required('food.can_serve', raise_exception=True)
def prepare(request):
    orders = OrderInstance.objects.all()
    return render(request, "food/prepare.html", { 'orders':orders })
