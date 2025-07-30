from django import forms
from django.core.exceptions import ValidationError
from .models import RepicUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
import re
from .models import Product

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}))
    date_of_birth = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}))
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = RepicUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'password1', 'password2']
        widgets = {
            # 'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not re.match(r'^\+?1?\d{9,15}$', phone_number):
            raise ValidationError("Enter a valid phone number")
        return phone_number

class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = RepicUser
        fields = ['email', 'password']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class ProfileForm(forms.ModelForm):
    profile_picture = forms.FileField(required=False)
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3}), required=False)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=False)

    class Meta:
        model = RepicUser
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'bio']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 or password2:
            if password1 != password2:
                raise ValidationError('Passwords do not match.')
        return cleaned_data

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['user', 'created_at']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3, 'maxlength': 4096}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'subcategory': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '₹'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'condition': forms.TextInput(attrs={'class': 'form-control'}),
            'location_state': forms.TextInput(attrs={'class': 'form-control'}),
            'location_city': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'maxlength': 70}),
            'image1': forms.ClearableFileInput(attrs={'multiple': False}),
            'image2': forms.ClearableFileInput(attrs={'multiple': False}),
            'image3': forms.ClearableFileInput(attrs={'multiple': False}),
            'image4': forms.ClearableFileInput(attrs={'multiple': False}),
            'image5': forms.ClearableFileInput(attrs={'multiple': False}),
            'image6': forms.ClearableFileInput(attrs={'multiple': False}),
            'image7': forms.ClearableFileInput(attrs={'multiple': False}),
            'image8': forms.ClearableFileInput(attrs={'multiple': False}),
            'image9': forms.ClearableFileInput(attrs={'multiple': False}),
            'image10': forms.ClearableFileInput(attrs={'multiple': False}),
            'image11': forms.ClearableFileInput(attrs={'multiple': False}),
            'image12': forms.ClearableFileInput(attrs={'multiple': False}),
        }