from .models import Cart, CartItem

def cart_count(request):
    count = 0
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        count = cart.get_item_count()
    elif request.session.session_key:
        cart = Cart.objects.filter(session_key=request.session.session_key).first()
        if cart:
            count = cart.get_item_count()
    return {'cart_count': count}