from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic import TemplateView
from django.views.generic import CreateView
from myapp.models import Product
from myapp.forms import SignUpForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart

class ChavaView(TemplateView):
    template_name = 'chava.html'

class DetailDetailView(DetailView):
    model = Product
    template_name = 'detail.html'

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class Product_allView(TemplateView):
    template_name = 'product_all.html'

class Product_bowlView(TemplateView):
    template_name = 'product_bowl.html'

class Product_boxView(TemplateView):
    template_name = 'product_box.html'

class Product_cupView(TemplateView):
    template_name = 'product_cup.html'

class Product_cutleryView(TemplateView):
    template_name = 'product_cutlery.html'

class Product_plateView(TemplateView):
    template_name = 'product_plate.html'

class Product_strawView(TemplateView):
    template_name = 'product_straw.html'

class ContactView(TemplateView):
    template_name = 'contact.html'

class BillView(TemplateView):
    template_name = 'bill.html'

class CardView(TemplateView):
    template_name = 'card.html'

@login_required
def block(request):
    return render(request,'homepage.html')

def sign_up(request):
    context = {}
    form = SignUpForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return render(request,'homepage.html')
    context['form']=form
    return render(request,'registration/sign_up.html',context)

@login_required(login_url="/users/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')


