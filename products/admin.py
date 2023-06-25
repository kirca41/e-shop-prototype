from django.contrib import admin
from products.models import *


class OrderAdmin(admin.ModelAdmin):

    list_display = ['first_name', 'last_name', 'city', ]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


class ProductInShoppingCartAdmin(admin.ModelAdmin):

    list_display = ['shopping_cart_user', 'quantity', 'product']

    def shopping_cart_user(self, obj):
        return obj.shopping_cart.user

    shopping_cart_user.short_description = 'Shopping Cart User'

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


class ProductInOrderAdmin(admin.ModelAdmin):

    list_display = ['order_info', 'quantity', 'product']

    def order_info(self, obj):
        return f'{obj.order.first_name} {obj.order.last_name} - {obj.order.city}'

    order_info.short_description = 'Order Customer - City'

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(Manufacturer)
admin.site.register(Product)
admin.site.register(ProductInShoppingCart, ProductInShoppingCartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ProductInOrder, ProductInOrderAdmin)