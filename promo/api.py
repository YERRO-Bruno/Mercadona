from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Promotion
from rest_framework.pagination import PageNumberPagination
from .serializers import PromotionSerializer
from rest_framework import viewsets

@csrf_exempt
def api_exemple(request):
    if request.method =="GET":
        data = {"message": "GET request for retrieving data"}
        return JsonResponse(data)
    else:
        return HttpResponseNotAllowed


class  PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer
    pagination_class = PageNumberPagination

