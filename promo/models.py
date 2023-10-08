from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    role = models.ForeignKey("Role", null=True, blank=True, on_delete=models.SET_NULL)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email




class VerifAdmin(models.Model):
    email = models.CharField(max_length=64, null=False, unique=True)
    verification = models.CharField(max_length=128)

    def __str__(self):
        return self.email

    def getVerifAdmin(self):
        return {'id': self.id, 'email': self.email, 'verification': self.verification}



class Role(models.Model):
    label = models.CharField(max_length=64, null=False)

    def __str__(self):
        return self.label

    def getRole(selfself):
        return {'id': self.id, 'label': self.label}


class Category(models.Model):
    label = models.CharField(max_length=64, null= False)

    def __str__(self):
        return str(self.label)


class Product(models.Model):
    product_label = models.CharField(max_length=24)
    description = models.CharField(max_length=256)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image = models.CharField(null=True, max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    promo = models.OneToOneField ("Promotion", null=True, blank= True , on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.product_label)


class Promotion(models.Model):
    product_promo = models.OneToOneField("Product", on_delete=models.CASCADE)
    begin_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    percent_promo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.product_promo)

