from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .products import products
from .serializers import ProductSerializer 


# Create your views here.

@api_view(['GET'])
def getRoutes(request):
  routes = [
    '/api/products/',
    '/api/products/create/',
    '/api/proucts/upload/',
    '/api/proucts/<id>/reviews/',

    '/api/proucts/top/',
    
    '/api/proucts/<updata>/<id>/',
  ]
  return Response(routes)

@api_view(['GET'])
def getProducts(request):
  products = Product.objects.all()
  serializers = ProductSerializer(products, many=True)
  return Response(serializers.data)
""" def getProducts(request):
  return JsonResponse(products, safe=False) """

@api_view(['GET'])
def getProduct(request, pk):
  product = None
  for i in products:
    if i['_id'] == pk:
      product = i
      break
  return Response(product)