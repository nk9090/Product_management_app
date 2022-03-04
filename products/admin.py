from itertools import product
from django.contrib import admin
from . models import Product
from .models import Category
from . models import Comment

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display =('id','name','price','is_published','created_at')
    list_display_links=('id','name')
    list_filter= ('price','created_at')
    list_editable=('is_published',)
    search_fields=('name','price')
    ordering=('price',)

admin.site.register(Product,ProductAdmin )
admin.site.register(Category)
admin.site.register(Comment)