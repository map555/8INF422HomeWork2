from django.shortcuts import render
from TP2Q3.models import *
from TP2Q3.forms import *
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def Home(request):
    return render(request,"MenuBar.html")

def CarByIDHome(request):
    return render(request, "CarByID.html")

def get_car_info_by_id(request):
    if request.method == "GET" and request.is_ajax():
        carID=request.GET.get("car_id")
        testQuery=Car.objects.filter(id=carID).values('model')

        if(len(testQuery)!=0):
            car = Car.objects.get(id=carID)
            car_info={'manufacturer':car.manufacturer,
                    'model':car.model,
                    'cartrim':car.trim,
                    'mileage':car.mileage,
                    'caryear':car.year,
                    'carweight':car.weight,
                    'condition':car.condition,
                    'carcolor':car.color,
                    'price':car.price}
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

    return JsonResponse({"success":False}, status=400)

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

def BillFormView(request):
    billForm=BillForm()
    return render(request,'CreateBill.html',{"billform":billForm})

def PostBillForm(request):
    if request.method == "POST" and request.is_ajax():
        requestCarID=request.POST['carId']
        requestBuyerName=request.POST['buyerName']

        requestCar=None

        #Try to get the car of the form.
        try:
            requestCar=Car.objects.get(id=requestCarID)
        except (ObjectDoesNotExist):
            requestCar=None #requestCar is affected to "None" if objects.get return an "ObjectDoesNotExist" exception



        #Check if the
        if (requestCar!=None ):

            #Check if the car is sold
            if (requestCar.sold!=True):
                requestCar.sold = True
                requestCar.save()
                newBill=Bill()
                newBill.clientName=requestBuyerName
                newBill.Car=requestCar
                newBill.save()
                return JsonResponse({"success":True}, status=200)#valid good request


            else:
                return JsonResponse({"success":False}, status=206)#car was found but sold is true

        else:
            return JsonResponse({"success":False}, status=204)#car was not found


    return JsonResponse({"success":False},status=400)#bad request