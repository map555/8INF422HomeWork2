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
    path('car/carbyid',views.CarByIDHome,name="car_by_id_home"),
    path('ajax/get_car_info_by_id',views.get_car_info_by_id,name="get_car_info_by_id"),
    path('bills/create_bill',views.BillFormView,name="create_bill"),
    path('ajax/create_bill',views.PostBillForm,name="post_bill")



]+ static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
