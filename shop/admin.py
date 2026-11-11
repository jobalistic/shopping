from django.contrib import admin
from shop.models import Product,Order,UserProfile



class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name','category','quantity')
    list_filter = ['category']
    search_fields = ['name']

class OrderAdmin(admin.ModelAdmin):
    model = Order
    list_display = ('product','created_by','order_quantity','date')
    list_field = ['date']
    search_fields = ['product']


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    list_display = ('user',)
    list_filter = ['user']
    search_fields = ['user_username']

    
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(UserProfile,UserProfileAdmin)

admin.site_header = "shop admin"
