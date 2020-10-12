from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.files import File
from django.db.models import Count
from TP2Q3.models import *
# Create your views here.

def CarByID(request, carID):
    car=Car.objects.filter(id=carID).values('manufacturer','model','trim','mileage','year','weight','condition','color','price')


def CarByManufacturer(request, CarManufacturer):

    cars=Car.objects.filter(manufacturer=CarManufacturer).order__by('model').values('model',
            'trim','mileage','year','weight','condition','color','price')


def BillByID(request,billID):
    bill=Bill.objects.filter(id=billID).select_related('Car').values('clientName','Car__manufacturer',
            'Car__model','Car__trim','Car__mileage','Car__year','Car__weight','Car__condition','Car__color','Car__price')

def BillByClient(request,client):
    bills=Bill.objects.filter(clientName=client).select_related('Car').order_by('Car__manufacturer','Car__model').values(
        'clientName', 'Car__manufacturer','Car__model', 'Car__trim', 'Car__mileage', 'Car__year', 'Car__weight',
        'Car__condition', 'Car__color','Car__price')