from django.shortcuts import render
from .models import Order

# Create your views here.

# def order_list(request):
#     data = Order.objects.all().order_by('price') # 1 --> sql --> db : lazy