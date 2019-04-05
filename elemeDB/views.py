from django.shortcuts import render
from django.http import HttpResponse
from dbms.view_models import *


# Create your views here.
def welcome(request):
    orders = ElemedbViewOrder.objects.all().values()
    return HttpResponse(orders)
