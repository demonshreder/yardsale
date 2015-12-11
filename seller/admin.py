from django.contrib import admin
from seller.models import UserProfile, products

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(products)
