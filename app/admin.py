from django.contrib import admin
from .models import Farmer, Product

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'state', 'district', 'city')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'farmer', 'price', 'created_at', 'expiry_date', 'is_expired', 'image')
    list_filter = ('expiry_date', 'created_at', 'farmer')
    search_fields = ('name', 'farmer__name')

    def is_expired(self, obj):
        return obj.is_expired()
    is_expired.boolean = True  # Render as a boolean icon in the admin
