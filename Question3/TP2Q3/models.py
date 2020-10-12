from django.db import models
import datetime
# Create your models here.

yearChoice=[(y,y) for y in range (1950, datetime.date.today().year+1)]
conditionChoice=["very bad","bad","normal","good","very good","showroom"]

class Car(models.model):

    manufacturer=models.CharField(max_length=25)
    model=models.CharField(max_length=25)
    trim=models.CharField(max_length=50)
    mileage=models.PositiveSmallIntegerFieldIntegerField(default=0)
    year=models.IntegerField(choices=yearChoice,default=datetime.datetime.now().year)
    weigth=models.PositiveSmallIntegerField()
    condition=models.CharField(choices=conditionChoice,default=conditionChoice[2])
    color=models.CharField(max_length=25)
    price=models.PositiveSmallIntegerField()

    class Meta:
        verbose_name="Car"
        verbose_name_plural="Cars"

    def __str__(self):
        return str(self.id)

class Bill(models.model):

    clientName=models.CharField(max_length=50)
    Car=models.ForeignKey("Car",on_delete=models.CASCADE)

    class Meta:
        verbose_name="Bill"
        verbose_name_plural="Bills"




