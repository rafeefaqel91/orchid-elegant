from django.shortcuts import render

# Create your views here.
import json
import uuid
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from .models import Category, Product, Cart, CartItem, Order, OrderItem, ContactMessage
from .forms import UserRegisterForm, ContactForm

def get_cart(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
    else:
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        cart, created = Cart.objects.get_or_create(session_key=session_key)
    return cart

def home(request):
    featured_products = Product.objects.filter(featured=True, available=True)[:8]
    new_products = Product.objects.filter(available=True).order_by('-created_at')[:8]
    categories = Category.objects.all()
    return render(request, 'store/home.html', {
        'featured_products': featured_products,
        'new_products': new_products,
        'categories': categories,
    })

def product_list(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    
    category = request.GET.get('category')
    search = request.GET.get('search')
    
    if category:
        products = products.filter(category__slug=category)
    if search:
        products = products.filter(Q(name__icontains=search) | Q(description__icontains=search))
    
    return render(request, 'store/product_list.html', {
        'products': products,
        'categories': categories,
    })

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    related_products = Product.objects.filter(category=product.category, available=True).exclude(id=product.id)[:4]
    return render(request, 'store/product_detail.html', {
        'product': product,
        'related_products': related_products,
    })

def add_to_cart(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            product_id = data.get('product_id')
            quantity = data.get('quantity', 1)
            
            product = get_object_or_404(Product, id=product_id, available=True)
            cart = get_cart(request)
            
            cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
            if not created:
                cart_item.quantity += int(quantity)
            else:
                cart_item.quantity = int(quantity)
            cart_item.save()
            
            return JsonResponse({
                'success': True,
                'cart_count': cart.get_item_count(),
                'message': f'{product.name} added to cart!'
            })
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    
    return JsonResponse({'success': False, 'message': 'Invalid request'})

def update_cart(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            item_id = data.get('item_id')
            quantity = data.get('quantity')
            
            cart_item = get_object_or_404(CartItem, id=item_id)
            if quantity > 0:
                cart_item.quantity = quantity
                cart_item.save()
            else:
                cart_item.delete()
            
            cart = cart_item.cart
            return JsonResponse({
                'success': True,
                'item_total': float(cart_item.get_total()),
                'cart_total': float(cart.get_total()),
                'cart_count': cart.get_item_count(),
            })
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    
    return JsonResponse({'success': False, 'message': 'Invalid request'})

def remove_from_cart(request, item_id):
    if request.method == 'POST':
        cart_item = get_object_or_404(CartItem, id=item_id)
        cart = cart_item.cart
        cart_item.delete()
        
        return JsonResponse({
            'success': True,
            'cart_total': float(cart.get_total()),
            'cart_count': cart.get_item_count(),
        })
    
    return JsonResponse({'success': False})

def cart_view(request):
    cart = get_cart(request)
    cart_items = cart.items.all()
    return render(request, 'store/cart.html', {
        'cart_items': cart_items,
        'cart_total': cart.get_total(),
    })

@login_required
def checkout(request):
    cart = get_cart(request)
    cart_items = cart.items.all()
    
    if not cart_items:
        messages.warning(request, 'Your cart is empty!')
        return redirect('cart')
    
    if request.method == 'POST':
        # Generate order number
        order_number = f"ORD-{uuid.uuid4().hex[:8].upper()}"
        
        order = Order.objects.create(
            user=request.user,
            order_number=order_number,
            first_name=request.POST.get('first_name'),
            last_name=request.POST.get('last_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            address=request.POST.get('address'),
            city=request.POST.get('city'),
            state=request.POST.get('state'),
            zip_code=request.POST.get('zip_code'),
            country=request.POST.get('country'),
            total_amount=cart.get_total(),
        )
        
        for item in cart_items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.get_price,
            )
        
        # Send order confirmation email
        try:
            send_mail(
                f'Order Confirmation - {order_number}',
                f'Thank you for your order! Your order number is {order_number}. Total amount: ${order.total_amount}',
                settings.EMAIL_HOST_USER,
                [order.email],
                fail_silently=False,
            )
        except:
            pass
        
        # Clear cart
        cart_items.delete()
        
        messages.success(request, f'Order placed successfully! Order number: {order_number}')
        return redirect('order_history')
    
    return render(request, 'store/checkout.html', {
        'cart_items': cart_items,
        'cart_total': cart.get_total(),
    })

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'store/order_history.html', {'orders': orders})

def about(request):
    return render(request, 'store/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = form.save()
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact')
    else:
        form = ContactForm()
    
    return render(request, 'store/contact.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            # Send welcome email
            try:
                send_mail(
                    'Welcome to Orchid Elegant!',
                    f'Welcome {user.first_name}! Thank you for registering at Orchid Elegant. Start shopping now!',
                    settings.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False,
                )
            except:
                pass
            
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = UserRegisterForm()
    
    return render(request, 'store/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Merge guest cart with user cart
            if request.session.session_key:
                guest_cart = Cart.objects.filter(session_key=request.session.session_key).first()
                if guest_cart:
                    user_cart, created = Cart.objects.get_or_create(user=user)
                    for item in guest_cart.items.all():
                        user_item, created = CartItem.objects.get_or_create(
                            cart=user_cart,
                            product=item.product,
                            defaults={'quantity': item.quantity}
                        )
                        if not created:
                            user_item.quantity += item.quantity
                            user_item.save()
                    guest_cart.delete()
            
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'store/login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')