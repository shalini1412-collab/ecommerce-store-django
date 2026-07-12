from django.shortcuts import render, get_object_or_404
from .models import Product, Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout


def home(request):
    products = Product.objects.all()
    return render(request, "home.html", {"products": products})


def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    return render(request, "product_detail.html", {
        "product": product
    })
def add_to_cart(request, id):

    cart = request.session.get('cart', [])

    cart.append(id)

    request.session['cart'] = cart

    return render(request, "cart.html", {
        "cart": cart
    })
def register(request):

    if request.method == "POST":

        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            return render(request, "home.html")

    else:

        form = UserCreationForm()


    return render(request, "register.html", {
        "form": form
    })



def user_login(request):

    if request.method == "POST":

        username = request.POST["username"]

        password = request.POST["password"]

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:

            login(request,user)

            return render(request,"home.html")


    return render(request,"login.html")



def user_logout(request):

    logout(request)

    return render(request,"home.html")
def checkout(request):

    cart = request.session.get('cart', [])

    if not cart:
        return render(request, "checkout.html", {
            "message": "Your cart is empty"
        })


    for product_id in cart:

        product = Product.objects.get(id=product_id)

        Order.objects.create(
            user=request.user.username if request.user.is_authenticated else "Guest",
            product=product,
            quantity=1
        )


    request.session['cart'] = []


    return render(request, "checkout.html", {
        "message": "Order placed successfully!"
    })