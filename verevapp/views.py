from django.db.models import Count
from django.shortcuts import render
from django.views import View
from . models import Product

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