from django.shortcuts import render

# Create your views here.
def order(request):
    return render(request, "food/order.html")

def homepage(request):
    return render(request, "food/homepage.html")