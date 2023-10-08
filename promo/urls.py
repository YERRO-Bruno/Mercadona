from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'promotions', views.PromotionViewSet)
router.register(r'products', views.ProductViewSet)

urlpatterns = [
                path("", views.index, name="index"),
                path("register/", views.register, name="register"),
                path("connect/", views.connect, name="connect"),
                path("api/categories/", views.api_categories, name="api_categories"),
                path("api/", include(router.urls)),
                ]
