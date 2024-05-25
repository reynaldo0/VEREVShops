from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.home),
    path("home/", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("category/<slug:val>", views.CategoryView.as_view(), name='category'),
    path("proddetail/<int:pk>", views.ProductDetail.as_view(), name='proddetail'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

