import json

from django.shortcuts import render
from TP2Q3.models import *
from TP2Q3.forms import *
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.

def Home(request):
    return render(request, "MenuBar.html")


def CarByIDHome(request):
    return render(request, "CarByID.html")


def get_car_info_by_id(request):
    if request.method == "GET" and request.is_ajax():

        requestCar = None

        # try to get the car
        try:
            requestCar = Car.objects.get(id=request.GET.get("car_id"), sold=False)
        except(ObjectDoesNotExist):
            requestCar = None

        if (requestCar != None):
            car_info = {'manufacturer': requestCar.manufacturer,
                        'model': requestCar.model,
                        'cartrim': requestCar.trim,
                        'mileage': requestCar.mileage,
                        'caryear': requestCar.year,
                        'carweight': requestCar.weight,
                        'condition': requestCar.condition,
                        'carcolor': requestCar.color,
                        'price': requestCar.price}
        else:
            car_info = {'manufacturer': "NULL",
                        'model': "NULL",
                        'cartrim': "NULL",
                        'mileage': "NULL",
                        'caryear': "NULL",
                        'carweight': "NULL",
                        'condition': "NULL",
                        'carcolor': "NULL",
                        'price': "NULL"}

        return JsonResponse({"car_info": car_info}, status=200)

    return JsonResponse({"success": False}, status=400)


def BillByIDHome(request):
    return render(request, "BillByID.html")

def CarCreated(request):
    return render(request, "success.html")


def get_bill_info_by_id(request):
    if request.method == "GET" and request.is_ajax():

        requestBill = None

        # try to get the car
        try:
            requestBill = Bill.objects.get(id=request.GET.get("bill_id"))
        except(ObjectDoesNotExist):
            requestBill = None

        if (requestBill != None):
            requestCar = Car.objects.get(id=requestBill.Car.id)
            bill_info = {'id': requestBill.id,
                         'clientName': requestBill.clientName,
                         'carPrice': requestCar.price}
        else:
            bill_info = {'id': "NULL",
                         'clientName': "NULL",
                         'carPrice': "NULL"}

        return JsonResponse({"bill_info": bill_info}, status=200)

    return JsonResponse({"success": False}, status=400)


def CarByManufacturer(request, CarManufacturer):
    cars = Car.objects.filter(manufacturer=CarManufacturer).order__by('model').values('model',
                                                                                      'trim', 'mileage', 'year',
                                                                                      'weight', 'condition', 'color',
                                                                                      'price')


def BillByID(request, billID):
    bill = Bill.objects.filter(id=billID).select_related('Car').values('clientName', 'Car__manufacturer',
                                                                       'Car__model', 'Car__trim', 'Car__mileage',
                                                                       'Car__year', 'Car__weight', 'Car__condition',
                                                                       'Car__color', 'Car__price')


def CarFormView(request):
    if request.method == "POST":
        carForm = AddCarForm(request.POST)
        if carForm.is_valid():
            newCar = carForm.save(commit=False)
            newCar.save()
            return redirect('http://localhost:8000/cars/car_created')
    else:
        carForm = AddCarForm()
    return render(request, 'CreateCar.html', {"form": carForm})


def BillFormView(request):
    billForm = BillForm()
    return render(request, 'CreateBill.html', {"billform": billForm})


def PostBillForm(request):
    status = 400
    if request.method == "POST" and request.is_ajax():
        requestCarID = request.POST['carId']
        requestBuyerName = request.POST['buyerName']

        requestCar = None

        # Try to get the car of the form.
        try:
            requestCar = Car.objects.get(id=requestCarID)
        except (ObjectDoesNotExist):
            requestCar = None  # requestCar is affected to "None" if objects.get return an "ObjectDoesNotExist" exception

        # Check if the
        if (requestCar != None):

            # Check if the car is sold
            if (requestCar.sold != True):
                requestCar.sold = True
                requestCar.save()
                newBill = Bill()
                newBill.clientName = requestBuyerName
                newBill.Car = requestCar
                newBill.save()

                status = 201  # request status
                return JsonResponse({"requestsuccess": True, "status": status}, status=status)  # valid good request


            else:
                status = 206
                return JsonResponse({"requestsuccess": False, "status": status},
                                    status=status)  # car was found but sold is true

        else:
            status = 206
            return JsonResponse({"requestsuccess": False, "status": 204}, status=status)  # car was not found

    return JsonResponse({"requestsuccess": False, "status": status}, status=status)  # bad request


def BillsByClientView(request):
    return render(request,"SelectBillsByClient.html")



def BillsByClient(request):
    if request.method == "GET" and request.is_ajax():
        bills=Bill.objects.filter(clientName=request.GET.get("client_name")).select_related('Car').order_by('id').values(
             'id','Car__manufacturer','Car__model', 'Car__trim','Car__year', 'Car__mileage','Car__color','Car__price')

        return JsonResponse({"bills":list(bills)},status=200)

    return JsonResponse({"success":False},status=400)