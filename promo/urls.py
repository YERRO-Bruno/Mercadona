import os
from pathlib import Path
from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
                path("", views.index, name="index"),
                path("administration/", views.administration, name="administration"),
                path("register/", views.register, name="register"),
                path("connect/", views.connect, name="connect"),
                path("logout/", views.logout, name="logout"),
                path("api/categories/", views.api_categories, name="api_categories"),
                path("api/", include(router.urls)),
                path('administration/upload_image/', views.upload_image, name='upload_image'),
                ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


