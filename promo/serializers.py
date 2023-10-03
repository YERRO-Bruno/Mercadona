from .models import Promotion, Product
from rest_framework import serializers


class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['percent_promo', 'begin_date', 'end_date']

class ProductSerializer(serializers.ModelSerializer):
    promo = PromotionSerializer()
    class Meta:
        model = Product
        fields = ['product_label', 'description', 'category', 'price', 'image', 'promo']



