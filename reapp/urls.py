from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('base/', views.base, name='base'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('sell/', views.add_product, name='add_product'),   
    path('post/', views.post_ad, name='post_ad'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout')
 ]