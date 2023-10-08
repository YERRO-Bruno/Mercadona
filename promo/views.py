from .models import Promotion, Product, Category, User, VerifAdmin, Role
from django.shortcuts import render,redirect
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import PromotionSerializer, ProductSerializer
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .managers import UserManager

def index(request):
    #product_list = Product.objects.all()
    #context = {"product_list" : product_list}

    return render(request , "index.html")

#Inscription administrateur
def register(request):
    if request.method == 'POST':
       emailx = request.POST['email']
       passwordx = request.POST['password']
       verificationx = request.POST['verification']
       verif_admins = VerifAdmin.objects.all()
       for i in range(len(verif_admins)):
            if (verif_admins[i].email == emailx and verif_admins[i].verification == verificationx ) :
                roles = Role.objects.all()
                Userx = User.objects.create_user( email = emailx, password = passwordx)
                for i in range(len(roles)):
                    if roles[i].label == "admin":
                        rolex = roles[i]
                Userx.role = rolex
                Userx.save()
                # suppression de l'enregistrememnt du code de verification et de l'email associée
                verif_admins[i].delete()
                return render(request, 'administration.html')
       #Pas autentifié
       return render(request, 'index.html', {'login': '---------'} )
    else:
        return render(request, 'register.html',)

def connect(request):
    if request.method == 'POST':
        emailx = request.POST['email']
        passwordx = request.POST['password']
        userx = authenticate(email=emailx, password=passwordx)
        if userx is not None:
            return render(request, 'index.html', {'login': emailx})
        else:
            return render(request, 'index.html', {'login': 'connectez-vous'} )

    else:
        return render(request, 'connect.html')



def api_categories(request):
    categories = Category.objects.all()
    #categories_json = [{'id': category.id, 'label': category.label} for category in categories]
    categories_json = [{'label': category.label} for category in categories]
    return JsonResponse(categories_json, safe = False)

def api_products(request):
    products = Product.objects.all()
    products_json = [{'id': product.id, 'product_label': product.product_label, 'description': product.description,
        'category_id': product.category_id, 'price': product.price, 'image': product.image} for product in products]
    return JsonResponse(products_json, safe = False)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

#CRUD VerifAdmin
#UPLOAD VerifAdin

#CREATE VerifAdin

#UPDATE VerifAdin

#DELETE VerifAdin




