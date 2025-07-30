from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import RegistrationForm, LoginForm, ProfileForm
import base64
from .models import RepicUser, Product

def home(request):
    return render(request, 'reapp/home.html')
    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = form.cleaned_data['email']  # Set username to email
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.email = form.cleaned_data['email']
            user.phone_number = form.cleaned_data['phone_number']
            user.date_of_birth = form.cleaned_data['date_of_birth']
            user.save()
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'reapp/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                user_obj = RepicUser.objects.get(email=email)
                user = authenticate(username=user_obj.username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('base')
            except RepicUser.DoesNotExist:
                pass
    else:
        form = LoginForm()
    return render(request, 'reapp/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

def base(request):
    return render(request, 'reapp/base.html')


def dashboard(request):
    return render(request, 'reapp/base.html')


def profile(request):
    user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user = form.save(commit=False)
            if form.cleaned_data.get('password1'):
                user.set_password(form.cleaned_data['password1'])
            if request.FILES.get('profile_picture'):
                user.profile_picture = request.FILES['profile_picture'].read()
            user.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = ProfileForm(instance=user)
    profile_picture_base64 = None
    if user.profile_picture:
        profile_picture_base64 = base64.b64encode(user.profile_picture).decode('utf-8')
    return render(request, 'reapp/profile.html', {'form': form, 'profile_picture_base64': profile_picture_base64, 'user': user})


def add_product(request):
    if request.method == 'POST':
        # Handle form submission
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        condition = request.POST.get('condition')
        brand = request.POST.get('brand')
        location = request.POST.get('location')
        category = request.POST.get('category')
        subcategory = request.POST.get('subcategory')
        
        # Create and save the product
        try:
            product = Product.objects.create(
                user=request.user,
                title=title,
                price=price,
                description=description,
                condition=condition,
                brand=brand,
                location_city=location,  # Using location_city for the location field
                category=category,
                subcategory=subcategory
            )
            messages.success(request, f'Ad "{title}" posted successfully!')
            return redirect('post_ad')
        except Exception as e:
            messages.error(request, f'Error posting ad: {str(e)}')
            return redirect('add_product')
    
    return render(request, 'reapp/add_product.html')


def post_ad(request):
    return render(request, 'reapp/post_ad.html')


