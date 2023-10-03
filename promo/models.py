from django.db import models


class User(models.Model):
    email = models.CharField(max_length=64, unique=True)
    hashed_password = models.CharField(max_length=64)
    firstname = models.CharField(max_length=31)
    lastname = models.CharField(max_length=31)
    role = models.ForeignKey("Role", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.email


class Role(models.Model):
    label = models.CharField(max_length=32)

    def __str__(self):
        return str(self.label)


class Category(models.Model):
    label = models.CharField(max_length=64)

    def __str__(self):
        return str(self.label)


class Product(models.Model):
    product_label = models.CharField(max_length=24)
    description = models.CharField(max_length=256)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    image = models.CharField(null=True, max_length=64)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    promo = models.ForeignKey("Promotion", null=True,on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.product_label)


class Promotion(models.Model):
    #product_promo = models.OneToOneField("Product", on_delete=models.CASCADE)
    begin_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    percent_promo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.product_promo)

