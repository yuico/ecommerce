from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

def getProducts(request):
  return JsonResponse(products, safe=False)