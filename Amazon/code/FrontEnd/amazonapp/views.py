from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django import template
from .forms import SignupForm, AddItemToCart, DeliverInfo, CartForm, SearchItem
from .models import Cart, Order, PurchasedProduct, Warehouse
from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, FormView
from django.template.defaulttags import register
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
import socket

# Create your views here.

back_end_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try: 
    back_end_socket.connect(("vcm-12231.vm.duke.edu", 65432))
except BaseException as e:
    print("Migrating...")

def receive_backend_response():
    front_end_request = ""
    bit = back_end_socket.recv(1)
    bit = bit.decode()
    while bit != "\n":
        front_end_request += bit
        bit = back_end_socket.recv(1)
        bit = bit.decode()
    return front_end_request

class CartDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Cart
    template_name = 'item_delete.html'
    success_url = '/amazon/myCart' 
    
    def delete(self, request, *args, **kwargs):
        return super(CartDeleteView, self).delete(request, *args, **kwargs)

    def test_func(self):
        cart = self.get_object()
        if self.request.user == cart.userid:
            return True
        return False


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', context={'form': form})

@login_required(login_url='../accounts/login/')
def search_item(request):
    if request.method == 'POST':
        form = SearchItem(request.POST)
        if form.is_valid():
            url = form.cleaned_data['item_name'] + "/Add"
            return redirect(url)
    else:
        form = SearchItem()

    return render(request, 'search_item.html', context={'form': form})

@login_required(login_url='../accounts/login/')
def add_to_cart(request, product_name):
    if request.method == 'POST':
        form = AddItemToCart(request.POST)
        if form.is_valid():
            current_cart = Cart
            if current_cart.objects.filter(product_name = product_name, userid = request.user).exists():
                current_product = get_object_or_404(Cart, pk=product_name)
                current_product.count += form.cleaned_data['quantity']
                current_product.save()
            else:
                cart = Cart()
                cart.userid = request.user
                cart.product_name = product_name
                cart.count = form.cleaned_data['quantity']
                cart.save()
            messages.success(request, 'item added!')
            back_end_request = "purchase more:" + product_name + "-" + str(form.cleaned_data['quantity']) + "\n"
            back_end_socket.send(back_end_request.encode())
            return redirect('/')
    else:
        form = AddItemToCart()
    return render(request, 'add_item.html', context={'form': form, 'product_name':product_name})

class check_my_cart(LoginRequiredMixin, ListView):
    model = Cart
    template_name = 'check_my_cart.html'
    context_object_name = 'qs'
    def get_queryset(self):
        qs = Cart.objects.filter(userid=self.request.user)
        return qs
        
@login_required(login_url='../accounts/login/')
def place_order(request):
    if request.method == 'POST':
        form = DeliverInfo(request.POST)
        if form.is_valid():
            locationx = form.cleaned_data["location_x"]
            locationy = form.cleaned_data["location_y"] 
            ups_name = form.cleaned_data["ups_username"]
            user_cart = Cart.objects.filter(userid = request.user)
            products = ""
            for (i, product) in enumerate(user_cart):
                inventory = get_object_or_404(Warehouse, product_name = product.product_name)
                if inventory.total_number < product.count:
                    order_status = "Order failed:" + product.product_name + " is out of stock"
                    messages.success(request, order_status)
                    return redirect('/')
                products += product.product_name + "," + str(product.count) + "-"
            products = products[:-1]
            back_end_request = "new order:" + str(request.user.id) + "-" + products + "-" + str(locationx) + "-" + str(locationy) + "-" + ups_name + "\n"
            back_end_socket.send(back_end_request.encode())
            messages.success(request, "Order succeed!")
            return redirect('/')
    else:
        form = DeliverInfo(initial = {"location_x": request.user.location_x, "location_y": request.user.location_y, "ups_username": request.user.ups_name})
    return render(request, 'place_order.html', context={'form': form})

class view_my_order(LoginRequiredMixin, ListView):
    template_name = 'order_list_1.html'
    context_object_name = 'order_list'
    def get_queryset(self):   
        return Order.objects.filter(owner = self.request.user)
        
class CartUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Cart
    fields = ['count']
    template_name =  'item_update.html'
    
    def form_valid(self, form):
        item = self.get_object()
        item.count = form.cleaned_data.get('count')
        back_end_request = "purchase more:" + item.product_name+ "-" + str(item.count) + "\n"
        back_end_socket.send(back_end_request.encode())
        item.save()
        return super(CartUpdateView, self).form_valid(form)

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.userid:
            return True
        return False 

    def get_success_url(self):
        messages.success(self.request, 'Cart Updated')
        success_url = '/amazon/myCart' 
        return success_url

'''
@login_required
def CartUpdateView(request, cart_pk):
    template_name = 'item_update.html'

    form = CartForm()
    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            new_count = form.cleaned_data.get("count")
            item = Cart.objects.get(pk = cart_pk)
            item.count = new_count
            item.save()
            back_end_request = "purchase more:" + item.product_name+ "-" + str(new_count) + "\n"
            back_end_socket.send(back_end_request.encode())

        return redirect("/amazon/myCart")

    else:
        return render(request, template_name, context = { "form"})
'''