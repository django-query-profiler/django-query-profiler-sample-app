from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url="accounts:login")
def order(request):
    return render(request, "food/order.html")

@login_required(login_url="accounts:login")
def homepage(request):
    return render(request, "food/homepage.html")