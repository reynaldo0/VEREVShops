from django.db.models import Count
from django.shortcuts import render, redirect
from django.views import View
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

def show_cart(req):
    user = req.user
    cart = Cart.objects.filter(user=user)
    return render(req, 'addcart.html', locals())