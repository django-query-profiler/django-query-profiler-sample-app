from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

@permission_required('food.can_order')
def order(request):
    return render(request, "food/order.html")

@login_required(login_url="accounts:login")
def homepage(request):
    return render(request, "food/homepage.html")

@permission_required('food.can_serve')
def prepare(request):
    return render(request, "food/prepare.html")