from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('food.can_order', raise_exception=True)
def order(request):
    return render(request, "food/order.html")

def homepage(request):
    return render(request, "food/homepage.html")

@login_required
@permission_required('food.can_serve', raise_exception=True)
def prepare(request):
    return render(request, "food/prepare.html")
