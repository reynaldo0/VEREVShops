from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY_CHOICES=(
    ('CF', 'Coffe'),
    ('DS', 'Dessert'),
)

AREA_CHOICES = {
    ('KALIMANTAN','KALIMANTAN'),
    ('SUMATERA','SUMATERA'),
    ('JAWA','JAWA'),
    ('SULAWESI','SULAWESI'),
    ('PAPUA','PAPUA'),
}

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models. TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title
    def fselling_price(self):
        return "Rp. {:,.3f}".format(self.selling_price).replace(',', '.') #Format biar bisa ada 0 setelah koma

    def fdiscounted_price(self):
        return "Rp. {:,.3f}".format(self.discounted_price).replace(',', '.') #Format biar bisa ada 0 setelah koma
    
    def getCategory(self):
        return dict(CATEGORY_CHOICES).get(self.category, self.category) # Membuat agar yang tampil kepanjangan nama kategori
    
    def get_all_categories():
        return ', '.join([label for _, label in CATEGORY_CHOICES]) # mengambil semua kategori yang ada
    
class Customer(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    mobile = models.IntegerField()
    zipcode = models.IntegerField()
    state = models.CharField(choices=AREA_CHOICES, max_length=100)
    
    def __str__(self):
        return self.name
    