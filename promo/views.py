from .models import Product, Category, User, VerifAdmin, Role
from django.shortcuts import render,redirect, get_object_or_404
from django.http import JsonResponse
from rest_framework import viewsets
from .serializers import ProductSerializer
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .managers import UserManager
from django.http import HttpResponse
from django.template import RequestContext
from django.template.context_processors import csrf
from .views import redirect
import os

def index(request):
    print(DEBUG)
    return render(request , "index.html")

def administration(request):
    print(DEBUG)
    emailx = request.session.get('email')
    passwordx = request.session.get('password')

    if request.method == 'POST':
        print("admin")
        print(request.session.get('email'))
        emailx = request.session.get('email')
        passwordx = request.session.get('password')
        userConnected = authenticate(email=emailx, password=passwordx)
        if userConnected is not None:
            print("connect")
            login(request, userConnected)
            action = request.POST.get('action', '')
            idx = request.POST['prodid']
            btnx = request.POST['BTN']
            addcatx = request.POST['addcat']
            imgx = request.POST['fileimage']
            labelx = request.POST['label']
            descriptionx = request.POST['description']
            print(request.POST['addcat'])
            catx =  request.POST['categ']
            pricex = request.POST['price']
            promox = request.POST['promo']
            beginx = request.POST['begin']
            endx = request.POST['end']
            context= {}
            context['prodid'] = idx
            context['label'] = labelx
            # print(context)
            if btnx == "addcat":
                print("addcat")
                retour = controlCategory(catx)
                if retour['result'] :
                    createCategory(catx)
                    messages.add_message(request, messages.INFO, "Catégorie ajoutée")
                    return render(request, "administration.html", context)
                else :
                    context['errorline'] = retour.errorline
                    return render(request, "administration.html", context)

            if btnx == "new":
                print("create")
                if idx != "0":
                    messages.add_message(request, messages.INFO, "vous devez 'Effacer les champs' avant de 'créer produit'")
                    return render(request, "administration.html", context)
                else:
                    controleProduct()
                    print("create2")
                    createProduct(labelx, descriptionx, catx, imgx, pricex,promox, beginx, endx)
                    print(imgx)
                    messages.add_message(request, messages.INFO, "Produit ajoutéé")
                    return render(request, "administration.html")
            if btnx == "updat":
                controleProduct()
                updateProduct(idx, labelx, descriptionx, catx, imgx, pricex, promox, beginx, endx)
                messages.add_message(request, messages.INFO, "Produit modifié")
                return render(request, "administration.html", context)
            if btnx == "suppr":
                deleteProduct(idx)
                messages.add_message(request, messages.INFO, "Produit supprimé")
                return render(request, "administration.html")
        else:
            messages.add_message(request, messages.INFO, "Vous n' êtes pas connecté")
            return redirect("/promo/connect")
    else:
        return render(request , "administration.html")



def logout(request):
    #logout(request)
    messages.add_message(request, messages.INFO, "Vous êtes déconnecté")
    return redirect("/promo")


#Inscription administrateur
def register(request):
    if request.method == 'POST':
       emailx = request.POST['email']
       passwordx = request.POST['password']
       verificationx = request.POST['verification']
       verif_admins = VerifAdmin.objects.all()
       #recherche du cpde de verification pour l'email de l'administrateur à créer
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
                #connexion
                return redirect('/promo/connect')
       #Pas autentifié
       messages.add_message(request, messages.INFO, "Vous n' avez pas été authentifié." )
       return redirect('/promo/register')
    else:
        return render(request, 'register.html')

def connect(request):
    if request.method == 'POST':
        emailx = request.POST['email']
        passwordx = request.POST['password']
        userConnected = authenticate(email=emailx, password=passwordx)
        if userConnected is not None:
            print("connect")
            login(request, userConnected )
            request.session['email'] = emailx
            request.session['password'] = passwordx

            return redirect('/promo/administration')
        else:
            messages.add_message(request, messages.INFO, "Vous n' avez pas été authentifié")
            return render(request, 'connect.html', {'errorLogin': "Email et/ou mot de passe erroné"})
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


def createProduct(prodlab, proddesc, prodcat, prodimg, prodprice, prodreduc, prodbegin, prodend):
        print ("createprod")
        prodx = Product()
        prodx.product_label = prodlab
        prodx.description = proddesc
        prodx.category = Category.objects.get(label=prodcat)
        prodx.image = prodimg
        prodx.price = prodprice
        prodx.reduction = prodreduc
        prodx.begin_promo = prodbegin
        prodx.end_promo = prodend
        prodx.save()


def updateProduct(prodid, prodlab, proddesc, prodcat, prodimg, prodprice, prodreduc, prodbegin, prodend):
    prodx = Product.objects.get(id=prodid)
    prodx.product_label = prodlab
    prodx.description = proddesc
    prodx.category = prodcat
    prodx.image = prodimg
    prodx.price = prodprice
    prodx.reduction = prodreduc
    prodx.begin_promo = prodbegin
    prodx.end_promo = prodend
    prodx.save()


def deleteProduct(prodid):
        prodx = Product.objects.get(id=prodid)
        prodx.delete()


def createCategory(categ):
    categx = Category()
    categx.label = categ
    categx.save()


def controlCategory(cat):
    if type(cat) != str:
        print("categorie n'est pas une chaine")
        return({'result': False, 'errorline': 'la catégorie doit être une chaine de caractère !'})
    else :
        return ({'result': True})




def controleProduct():
    print("control product")


def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        destination_path = os.path.join('static/images', image.name)
        with open(destination_path, 'wb') as f:
            for chunk in image.chunks():
                f.write(chunk)
        return JsonResponse({'message': 'Image téléchargée avec succès'})
    return JsonResponse({'message': 'Échec du téléchargement de l\'image'}, status=400)






