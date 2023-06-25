from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .forms import ProductForm, OrderForm
from .models import *


def index(request):
    order_by = request.GET.get('order_by')
    if order_by is None:
        qs = Product.objects.all()
    else:
        qs = Product.objects.all().order_by(order_by).values()
    context = { 'products': qs, 'selected': order_by }

    return render(request, 'index.html', context)


def product_details(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = { 'product': product }

    return render(request, 'product_details.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Replace 'home' with the name of your homepage URL pattern
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product = Product(
                name=form.cleaned_data['name'],
                model=form.cleaned_data['model'],
                image_url=form.cleaned_data['image_url'],
                price=form.cleaned_data['price'],
                quantity=form.cleaned_data['quantity'],
                description=form.cleaned_data['description'],
                category=form.cleaned_data['category'],
                manufacturer=form.cleaned_data['manufacturer']
            )
            product.save()
            return redirect("index")
    else:
        form = ProductForm()

    context = {
        'form': form,
    }

    return render(request, "add_product.html", context)


def categories(request):
    category_list = [choice[0] for choice in Product.CATEGORY_CHOICES]

    context = { 'categories': category_list }

    return render(request, "categories.html", context)


def guitar_category(request):
    qs = Product.objects.filter(category='GUITARS')
    context = {'products': qs}
    return render(request, 'index.html', context)


def keyboard_category(request):
    qs = Product.objects.filter(category='KEYBOARDS')
    context = {'products': qs}
    return render(request, 'index.html', context)


def percussion_category(request):
    qs = Product.objects.filter(category='PERCUSSION')
    context = {'products': qs}
    return render(request, 'index.html', context)


def amplifiers_category(request):
    qs = Product.objects.filter(category='AMPLIFIERS')
    context = {'products': qs}
    return render(request, 'index.html', context)


def cables_category(request):
    qs = Product.objects.filter(category='CABLES')
    context = {'products': qs}
    return render(request, 'index.html', context)


def shopping_cart(request):
    qs = ProductInShoppingCart.objects.filter(shopping_cart__user=request.user)
    total_price = 0.0

    for p in qs:
        total_price += float(p.quantity * p.product.price)

    context = {'products': qs, 'total_price': total_price }

    return render(request, 'shopping_cart.html', context)


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart, created = ShoppingCart.objects.get_or_create(user=request.user)

    # Check if the product already exists in the shopping cart
    product_in_cart, created = ProductInShoppingCart.objects.get_or_create(product=product, shopping_cart=cart, quantity=1)

    # Increase the quantity if the product is already in the cart, otherwise set it to 1
    if created:
        product_in_cart.quantity = 1
    else:
        product_in_cart.quantity += 1

    product_in_cart.save()

    return redirect('shopping_cart')


def remove_from_shopping_cart(request, product_id):
    product_in_cart = get_object_or_404(ProductInShoppingCart, id=product_id)

    product_in_cart.delete()
    return redirect('shopping_cart')


def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            cart = get_object_or_404(ShoppingCart, user=request.user)
            products_in_cart = cart.productinshoppingcart_set.all()

            for product_in_cart in products_in_cart:
                quantity = product_in_cart.quantity
                product = product_in_cart.product

                ProductInOrder.objects.create(
                    quantity=quantity,
                    order=order,
                    product=product
                )

            cart.productinshoppingcart_set.all().delete()

            return redirect('index')
    else:
        form = OrderForm()

    context = {'form': form}
    return render(request, 'checkout.html', context)