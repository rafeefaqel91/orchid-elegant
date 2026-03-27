from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Category, Product, Cart, CartItem, Order, OrderItem, ContactMessage

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'available', 'featured']
    list_filter = ['category', 'available', 'featured']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'user', 'total_amount', 'status', 'created_at']
    list_filter = ['status', 'created_at']
    search_fields = ['order_number', 'user__username', 'email']
    inlines = [OrderItemInline]

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)