from django.contrib import admin
from .models import Product, Order

# Register your models here.

# admin.site.register(Product)
# admin.site.register(Order)
admin.site.site_header = "E-commerce Admin"
admin.site.site_title = "E-commerce Admin Portal"
admin.site.index_title = "Welcome to the E-commerce Admin Portal"


class ProductAdmin(admin.ModelAdmin):
    def change_category_to_default(self, request, queryset):
        queryset.update(category="default")
    change_category_to_default.short_description="Change category to default"
    list_display = ('name', 'price', 'quantity', 'category', 'discounted_price')
    search_fields =('name', 'category')
    actions=['change_category_to_default']
    fields = ('name', 'price')
    list_editable = ('price', 'quantity', 'category', 'discounted_price')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'total_price', 'state')
    search_fields = ('name', 'email')

admin.site.register(Order, OrderAdmin)

admin.site.register(Product, ProductAdmin)