from django.shortcuts import render
from django.views import View

# Create your views here.
def home(req):
    return render(req, 'index.html', {})

class CategoryView(View):
    def get(self, req, val):
        return render(req, 'category.html', locals())