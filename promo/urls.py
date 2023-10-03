from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from . import api


router = DefaultRouter()
router.register(r'/promotions', views.PromotionViewSet)
router.register(r'/products', views.ProductViewSet)

urlpatterns = [
                  path("", views.index, name="index"),
                  path("api/categories/", views.api_categories, name="api_categories"),
                  #path("api/products/", views.api_products, name="api_products"),
                  path("api", include(router.urls))

              ]
