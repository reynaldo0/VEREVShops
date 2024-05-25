from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm

urlpatterns = [
    path("", views.home),
    path("home/", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("category/<slug:val>", views.CategoryView.as_view(), name='category'),
    path("proddetail/<int:pk>", views.ProductDetail.as_view(), name='proddetail'),

    # Regist & Login Auth
    path("regist/", views.CustomerRegistView.as_view(), name='regist'),
    path("login/", auth_view.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

