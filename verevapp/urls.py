from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordChangeForm

urlpatterns = [
    path("", views.home),
    path("home/", views.home, name='home'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("category/<slug:val>", views.CategoryView.as_view(), name='category'),
    path("proddetail/<int:pk>", views.ProductDetail.as_view(), name='proddetail'),
    path("profile/", views.ProfileView.as_view(), name='profile'),
    path("setting/", views.setting, name='setting'),
    path("updateSetting/<int:pk>", views.updateSetting.as_view(), name='updateSetting'),
    path("add-cart/", views.add_cart, name='add-cart'),
    path("cart/", views.show_cart, name='showcart'),
    path("checkout/", views.show_cart, name='checkout'),

    # Regist & Login Auth
    path("regist/", views.CustomerRegistView.as_view(), name='regist'),
    path("login/", auth_view.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path("changepw/", auth_view.PasswordChangeView.as_view(template_name='changepw.html', form_class=MyPasswordChangeForm, success_url='/home'), name='changepw'),
    path("login/", auth_view.LogoutView.as_view(next_page='login'), name='logout'),
    
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

