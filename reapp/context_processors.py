import base64
from .models import Product

def profile_picture_base64(request):
    user = getattr(request, 'user', None)
    if user and user.is_authenticated and hasattr(user, 'profile_picture') and user.profile_picture:
        return {
            'profile_picture_base64': base64.b64encode(user.profile_picture).decode('utf-8')
        }
    return {
        'profile_picture_base64': None
    }

def latest_ad(request):
    latest = Product.objects.order_by('-created_at').first()
    return {'latest_ad': latest} 