from django.db.models import Count
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from . models import Cart, Customer, Product
from . forms import CustomerRegistForm, CustomerProfileForm
from django.contrib import messages

# Create your views here.
def home(req):
    products = Product.objects.all()
    coffee_products = Product.objects.filter(category='CF')
    dessert_products = Product.objects.filter(category='DS')
    all_category = Product.get_all_categories()
    return render(req, 'index.html', {
        'product': products, 
        'all_category': all_category,
        'coffee_products': coffee_products,
        'dessert_products': dessert_products,
    })

class CategoryView(View):
    def get(self, req, val):
        product = Product.objects.filter(category=val)
        title = Product.objects.filter(category=val).values('title')
        return render(req, 'category.html', locals())
    
class ProductDetail(View):
    def get(self, req, pk):
        product = Product.objects.get(pk=pk) #pk = primary key
        return render(req, 'proddetail.html', locals())
    
def about(req):
    return render(req, 'about.html')

def contact(req):
    return render(req, 'contact.html')

class CustomerRegistView(View):
    def get(self, req):
        form = CustomerRegistForm()
        return render(req, 'regist.html', locals())
    def post(self, req):
        form = CustomerRegistForm(req.POST)
        if form.is_valid():
            form.save()
            messages.success(req,"Selamat! Berhasil login")
            return redirect('login')
        else:
            messages.warning(req,"Data Yang Dimasukan Salah!")
        return render(req, 'regist.html', locals())
        
class ProfileView(View):
    def get(self, request):
        form = CustomerProfileForm()
        return render(request, 'profile.html', {'form': form})

    def post(self, request):
        form = CustomerProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            reg = Customer(user=user, name=name, locality=locality, city=city, mobile=mobile, state=state, zipcode=zipcode)
            reg.save()
            messages.success(request, "Selamat Profile Berhasil Di Update")
            return redirect('setting')  # Redirect ke halaman sukses setelah update profile
        else:
            messages.warning(request, "Data Yang Di Masukan Tidak Valid")
        return render(request, 'profile.html', {'form': form})
    
def setting(req):
    add = Customer.objects.filter(user= req.user)
    return render(req, 'setting.html', locals())

class updateSetting(View):
    def get(self, req, pk):
        add = Customer.objects.get(pk=pk)
        form = CustomerProfileForm(instance=add)
        return render(req, 'updateSetting.html', locals())

    def post(self, req, pk):
        form = CustomerProfileForm(req.POST)
        if form.is_valid():
            add = Customer.objects.get(pk=pk)
            add.name = form.cleaned_data['name']
            add.locality = form.cleaned_data['locality']
            add.city = form.cleaned_data['city']
            add.mobile = form.cleaned_data['mobile']
            add.state = form.cleaned_data['state']
            add.zipcode = form.cleaned_data['zipcode']
            add.save()
            messages.success(req, "Selamat Profile Berhasil Di Update")
        else:
            messages.warning(req, "Data Yang Di Masukan Tidak Valid")
        return redirect("setting")
    
def add_cart(req):
    user = req.user
    product_id = req.GET.get('prod_id')
    product = Product.objects.get(id = product_id)
    Cart(user=user, product=product).save()
    return redirect("/cart")

def format_rupiah(amount):
    return f"RP {amount:,.3f}".replace(',', '.')

def show_cart(request):
    user = request.user
    cart_items = Cart.objects.filter(user=user)
    
    amount = 0
    for item in cart_items:
        value = item.quantity * item.product.discounted_price
        amount += value
    
    totalamount = amount + 10  # Assuming 10 is the shipping cost
    
    # Format as Indonesian Rupiah
    formatted_amount = format_rupiah(amount)
    formatted_totalamount = format_rupiah(totalamount)
    formatted_shipping_cost = format_rupiah(10)
    
    return render(request, 'addcart.html', {
        'cart': cart_items,
        'amount': formatted_amount,
        'shipping_cost': formatted_shipping_cost,
        'totalamount': formatted_totalamount,
    })

def plus_cart(req):
    if req.method == 'GET':
        try:
            prod_id = req.GET['prod_id']
            print(f"Product ID: {prod_id}")
            
            if not Product.objects.filter(id=prod_id).exists():
                print("Invalid product ID.")
                return JsonResponse({'error': 'Invalid product ID'}, status=400)

            cart_items = Cart.objects.filter(Q(product_id=prod_id) & Q(user=req.user))
            if not cart_items.exists():
                print("Cart item does not exist.")
                return JsonResponse({'error': 'Cart item does not exist'}, status=404)
            
            c = cart_items.first()
            print(f"Cart item before update: {c}")
            
            c.quantity += 1
            c.save()
            print(f"Cart item after update: {c}")
            
            user = req.user
            cart = Cart.objects.filter(user=user)
            amount = 0
            for item in cart:
                value = item.quantity * item.product.discounted_price
                amount = amount + value
            
            totalamount = amount + 10
            # Format as Indonesian Rupiah
            formatted_amount = format_rupiah(amount)
            formatted_totalamount = format_rupiah(totalamount)
            
            data = {
                'quantity': c.quantity,
                'amount': formatted_amount,
                'totalamount': formatted_totalamount,
            }
            print(f"Response data: {data}")
            return JsonResponse(data)
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return JsonResponse({'error': str(e)}, status=500)

def minus_cart(req):
    if req.method == 'GET':
        try:
            prod_id = req.GET['prod_id']
            print(f"Product ID: {prod_id}")

            if not Product.objects.filter(id=prod_id).exists():
                print("Invalid product ID.")
                return JsonResponse({'error': 'Invalid product ID'}, status=400)

            cart_items = Cart.objects.filter(Q(product_id=prod_id) & Q(user=req.user))
            if not cart_items.exists():
                print("Cart item does not exist.")
                return JsonResponse({'error': 'Cart item does not exist'}, status=404)

            c = cart_items.first()
            print(f"Cart item before update: {c}")

            if c.quantity > 1:
                c.quantity -= 1
                c.save()
            else:
                c.delete()
                c = None

            user = req.user
            cart = Cart.objects.filter(user=user)
            amount = sum(item.quantity * item.product.discounted_price for item in cart)
            totalamount = amount + 10

            formatted_amount = format_rupiah(amount)
            formatted_totalamount = format_rupiah(totalamount)

            data = {
                'quantity': c.quantity if c else 0,
                'amount': formatted_amount,
                'totalamount': formatted_totalamount,
            }
            print(f"Response data: {data}")
            return JsonResponse(data)

        except Exception as e:
            print(f"An error occurred: {e}")
            return JsonResponse({'error': str(e)}, status=500)
    
def remove_cart(req):
    if req.method == 'GET':
        try:
            prod_id = req.GET['prod_id']
            print(f"Product ID: {prod_id}")

            if not Product.objects.filter(id=prod_id).exists():
                print("Invalid product ID.")
                return JsonResponse({'error': 'Invalid product ID'}, status=400)

            cart_items = Cart.objects.filter(Q(product_id=prod_id) & Q(user=req.user))
            if not cart_items.exists():
                print("Cart item does not exist.")
                return JsonResponse({'error': 'Cart item does not exist'}, status=404)

            c = cart_items.first()
            print(f"Cart item before deletion: {c}")

            c.delete()

            user = req.user
            cart = Cart.objects.filter(user=user)
            amount = sum(item.quantity * item.product.discounted_price for item in cart)
            totalamount = amount + 10

            formatted_amount = format_rupiah(amount)
            formatted_totalamount = format_rupiah(totalamount)

            data = {
                'quantity': 0,
                'amount': formatted_amount,
                'totalamount': formatted_totalamount,
            }
            print(f"Response data: {data}")
            return JsonResponse(data)

        except Exception as e:
            print(f"An error occurred: {e}")
            return JsonResponse({'error': str(e)}, status=500)