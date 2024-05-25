from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm #lib auth dj
from django.contrib.auth.models import User

from .models import Customer

class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={
            'class': 'w-full p-2 border border-black bg-transparent backdrop-blur rounded-md placeholder:font-light placeholder:text-gray-500',
            'autofocus': 'True',
            'placeholder': 'Masukan Username Anda'
        })
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-2 border border-black bg-transparent backdrop-blur rounded-md placeholder:font-light placeholder:text-gray-500',
            'autocomplete':'current-password',
            'placeholder': 'Masukan Password Anda'
        })
    )

class CustomerRegistForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'autofocus': 'True',
            'class': 'w-full p-2 border border-black bg-transparent backdrop-blur rounded-md placeholder:font-light placeholder:text-gray-500',
            'placeholder': 'Masukan Username Anda'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'w-full p-2 border border-black bg-transparent backdrop-blur rounded-md placeholder:font-light placeholder:text-gray-500',
            'placeholder': 'Masukan Email Anda'
        })
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-2 border border-black bg-transparent backdrop-blur rounded-md placeholder:font-light placeholder:text-gray-500',
            'placeholder': 'Masukan Password Anda'
        })
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'w-full p-2 border border-black bg-transparent backdrop-blur rounded-md placeholder:font-light placeholder:text-gray-500',
            'placeholder': 'Konfirmasi Password Anda'
        })
    )

    class Meta:
        model = User
        fields = ['username','email']

class MyPasswordResetForm(PasswordChangeForm):
    pass

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','locality','city','mobile', 'state', 'zipcode']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-black bg-transparent backdrop-blur rounded-md placeholder:font-light placeholder:text-gray-500',
                'placeholder': 'Name'
            }),
            'locality': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-black bg-transparent backdrop-blur rounded-md placeholder:font-light placeholder:text-gray-500',
                'placeholder': 'Locality'
            }),
            'city': forms.TextInput(attrs={
                'class': 'w-full p-2 border border-black bg-transparent backdrop-blur rounded-md placeholder:font-light placeholder:text-gray-500',
                'placeholder': 'City'
            }),
            'mobile': forms.NumberInput(attrs={
                'class': 'w-full p-2 border border-black bg-transparent backdrop-blur rounded-md placeholder:font-light placeholder:text-gray-500',
                'placeholder': 'Mobile'
            }),
            'state': forms.Select(attrs={
                'class': 'w-full p-2 border border-black bg-transparent backdrop-blur rounded-md placeholder:font-light placeholder:text-gray-500',
                'placeholder': 'State'
            }),
            'zipcode': forms.NumberInput(attrs={
                'class': 'w-full p-2 border border-black bg-transparent backdrop-blur rounded-md placeholder:font-light placeholder:text-gray-500',
                'placeholder': 'Zipcode'
            }),
        }