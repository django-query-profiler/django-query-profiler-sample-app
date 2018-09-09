from django.shortcuts import render

def order(request):
    return render(request, "order.html")

def about(request):
    return render(request, "about.html")

def homepage(request):
    return render(request, "homepage.html")
