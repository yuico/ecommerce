from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .products import products


# Create your views here.

@api_view(['GET'])
def getRoutes(request):
  routes = [
    '/api/products',
    '/api/proucts/<id>/reviews',
    '/api/proucts/<id>',
  ]
  return Response(routes)

@api_view(['GET'])
def getProducts(request):
  products = Product.objects.all()
  return Response(products)
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