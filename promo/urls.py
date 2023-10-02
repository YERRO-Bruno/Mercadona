from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
                  path("", views.index, name="index"),
                  path("api/categories/", views.api_categories, name="api_categories"),
                  path("api/products/", views.api_products, name="api_products")
              ]
