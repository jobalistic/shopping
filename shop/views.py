from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from shop.forms import UserRegistry,ProductForm,OrderForm
from shop.models import Product,Order

@login_required
def index(request):
    order_user = Order.objects.all()
    user = User.objects.all()[:2]
    order_admin = Order.objects.all()[:2]
    products = Product.objects.all()[:2]
    reg_user = len(User.objects.all())
    all_prods = len(Product.objects.all())
    all_orders = len(Order.objects.all())
    
    context = {
        "title": "Home",
        "orders": order_user,
        "order_admin": order_admin,
        "users": users,
        "produts": products,
        "count_users": reg_user,
        "count_products": all_prods,
        "count_orders": all_orders,
        }
    return render(request,'shop/index.html',context)

@login_required
def products(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')
    else:
        form = ProductForm()
        context = {"title": products, "products":products,"form":form}
        return render(request,'shop/product.html',context)

@login_required
def orders(request):
    orders = Order.objects.all()
    print([i for i in request])
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.created_by = request.user
            instance.save()
            return redirect("orders")
    else:
        form = OrderForm()
    context = {"title": orders, "orders":orders, "form":form}
    return render(request,'shop/order.html',context)

@login_required
def users(request):
    user = User.objects.all()
    context = {"title": users, "users":users}
    return render(request,'shop/user.html',context)

def register(request):
    if request.method == 'POST':
        form = UserRegistry(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserRegistry()
    context = {"register":register, "form":form}
    return render(request,'shop/register.html',context)
        
