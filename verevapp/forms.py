from django import forms
from django.contrib.auth.forms import UserCreationForm #lib auth dj

class CustomerRegistForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'autofocus': 'True',
            'class': 'w-full p-2 border border-black bg-transparent backdrop-blur rounded-md placeholder:font-light placeholder:text-gray-500',
            'placeholder': 'Masukan Username Anda'
        })
    )
    email = forms.CharField(
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

    def __init__(self, *args, **kwargs):
        super(CustomerRegistForm, self).__init__(*args, **kwargs)
        self.order_fields(['username', 'email', 'password1', 'password2'])
