"""Question3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TP2Q3 import views
from django.conf.urls.static import *
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name="home"),
    path('bills/billbyid', views.BillByIDHome, name="bill_by_id_home"),
    path('car/carbyid',views.CarByIDHome,name="car_by_id_home"),
    path('car/carbymanufacturer', views.CarByManufacturerHome, name='car_by_manufacturer_home'),
    path('ajax/get_car_info_by_id',views.get_car_info_by_id,name="get_car_info_by_id"),
    path('ajax/get_car_info_by_manufacturer', views.get_car_info_by_manufacturer, name='get_car_info_by_manufacturer'),
    path('ajax/get_bill_info_by_id', views.get_bill_info_by_id, name="get_bill_info_by_id"),
    path('bills/create_bill',views.BillFormView,name="create_bill"),
    path('cars/create_car', views.CarFormView, name="create_car"),
    path('ajax/create_bill',views.PostBillForm,name="post_bill"),
    path('ajax/create_car', views.CarFormView, name="post_car"),
    path('cars/car_created', views.CarCreated, name="car_created")




]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
