from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

class RepicUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture = models.BinaryField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    
    # Fix for the reverse accessor clash
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_('The groups this user belongs to.'),
        related_name="customuser_groups",
        related_query_name="customuser",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="customuser_permissions",
        related_query_name="customuser",
    )
    
    def __str__(self):
        return self.username

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('mobile', 'Mobile Phones'),
        ('furniture', 'Furniture'),
        ('electronics', 'Electronics & Appliances'),
        ('fashion', 'Fashion'),
        ('books', 'Books, Sports & Hobbies'),
        ('pets', 'Pets'),
    ]
    SUBCATEGORY_CHOICES = [
        ('mobile_phones', 'Mobile Phones'),
        ('accessories', 'Accessories'),
        ('tablets', 'Tablets'),
        ('sofa_dining', 'Sofa & Dining'),
        ('beds_wardrobes', 'Beds & Wardrobes'),
        ('home_decor', 'Home Decor & Garden'),
        ('kids_furniture', 'Kids Furniture'),
        ('other_household', 'Other Household Items'),
        ('tvs', 'TVs, Video - Audio'),
        ('kitchen_appliances', 'Kitchen & Other Appliances'),
        ('computers', 'Computers & Laptops'),
        ('cameras', 'Cameras & Lenses'),
        ('games', 'Games & Entertainment'),
        ('men', 'Men'),
        ('women', 'Women'),
        ('kids', 'Kids'),
        ('books', 'Books'),
        ('gym', 'Gym & Fitness'),
        ('instruments', 'Musical Instruments'),
        ('sports', 'Sports Equipment'),
        ('hobbies', 'Other Hobbies'),
        ('fishes', 'Fishes & Aquarium'),
        ('pet_food', 'Pet Food & Accessories'),
        ('dogs', 'Dogs'),
        ('other_pets', 'Other Pets'),
    ]
    user = models.ForeignKey(RepicUser, on_delete=models.CASCADE)
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    subcategory = models.CharField(max_length=30, choices=SUBCATEGORY_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=50, blank=True, null=True)
    model = models.CharField(max_length=50, blank=True, null=True)
    condition = models.CharField(max_length=50, blank=True, null=True)
    location_state = models.CharField(max_length=50, blank=True, null=True)
    location_city = models.CharField(max_length=50, blank=True, null=True)
    image1 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image5 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image6 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image7 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image8 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image9 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image10 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image11 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    image12 = models.ImageField(upload_to='product_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.title} ({self.category} - {self.subcategory})"