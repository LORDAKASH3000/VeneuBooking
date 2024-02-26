# account/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from .models import Customuser

class CustomuserCreationForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class':'form-control form-control-lg'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password", 'class':'form-control form-control-lg'})
    )

    class Meta:
        model = Customuser
        fields = ['username', 'email', 'contactnumber', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-lg'}),
            'contactnumber': forms.TextInput(attrs={'class': 'form-control form-control-lg'})
        }
        labels = {
            'username': 'Username',
            'email': 'Email',
            'contactnumber': 'Contact Number',
            'password1': 'Password',
            'password2': 'Confirm Password',
        }
    
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if len(password1) < 8:
            self.add_error('password1', "Password must be at least 8 characters long.")

        if password1 != password2:
            self.add_error('password2', "Passwords do not match.")

        return cleaned_data

class CustomuserLoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(
            attrs={"autofocus": True, 'class': 'form-control w-75 mx-auto', 'aria-describedby':'emailHelp'}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", 'class':'form-control w-75 mx-auto', 'aria-describedby':'passHelp'}
        )
    )
    class Meta:
        model = Customuser
        fields = ['username', 'password']
        labels = {
            'username': 'Username',
            'password': 'Password'
        }