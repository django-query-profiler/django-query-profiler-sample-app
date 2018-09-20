from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import generics, permissions
from .forms import OrderForm
from .models import OrderInstance
from .serializers import OrderSerializer
from .permissions import IsBaristaOnly

@login_required
@permission_required('food.can_order', raise_exception=True)
def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            coffee_order = form.cleaned_data['coffee_order']
            # save OrderInstance to db
            customer_order = OrderInstance(name=name, email=email, coffee_order=coffee_order)
            customer_order.save()
            # set the pp_order (previous page order) key so user can view success page
            request.session['pp_order'] = True
            return redirect('food:success')
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

@login_required
def success(request):
    if 'pp_order' in request.session:
        del request.session['pp_order'] # delete the key so users won't be able to enter success page twice
        return render(request, "food/orderSuccess.html")
    else:
        return HttpResponseBadRequest('<h1>HTTP Error 400: You need to place an order!</h1>')

class OrderList(generics.ListCreateAPIView):
    queryset = OrderInstance.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderInstance.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsBaristaOnly,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)