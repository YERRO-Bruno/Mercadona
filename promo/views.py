from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category
from django.http import JsonResponse



def index(request):
    #product_list = Product.objects.all()
    #context = {"product_list" : product_list}

    return render(request , "index.html")


def api_categories(request):
    categories = Category.objects.all()
    categories_json = [{'id': category.id, 'label': category.label} for category in categories]
    return JsonResponse(categories_json, safe = False)

def api_products(request):
    products = Product.objects.all()
    products_json = [{'id': product.id, 'product_label': product.product_label, 'description': product.description,
        'category_id': product.category_id, 'price': product.price, 'image': product.image} for product in products]
    return JsonResponse(products_json, safe = False)