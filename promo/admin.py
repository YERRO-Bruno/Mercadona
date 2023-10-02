from django.contrib import admin

from .models import User, Role, Category, Product, Promotion

admin.site.register (User)
admin.site.register (Role)
admin.site.register (Category)
admin.site.register (Product)
admin.site.register (Promotion)