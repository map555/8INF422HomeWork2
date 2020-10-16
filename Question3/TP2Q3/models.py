from django.db import models
import datetime
# Create your models here.

yearChoice=[(y,y) for y in range (1950, datetime.date.today().year+1)]
conditionChoice=(("1","very bad"),("2","bad"),("3","normal"),
                 ("4","good"),("5","very good"),("6","showroom"))

class Car(models.Model):

    manufacturer=models.CharField(max_length=25)
    model=models.CharField(max_length=25)
    trim=models.CharField(max_length=50)
    mileage=models.PositiveSmallIntegerField(default=0)
    year=models.IntegerField(choices=yearChoice,default=datetime.datetime.now().year)
    weight=models.PositiveSmallIntegerField()
    condition=models.CharField(choices=conditionChoice,max_length=1,default=conditionChoice[2])
    color=models.CharField(max_length=25)
    price=models.PositiveSmallIntegerField()
    sold=models.BooleanField(default=False)

    class Meta:
        verbose_name="Car"
        verbose_name_plural="Cars"

    def __str__(self):
        return str(self.id)

class Bill(models.Model):

    clientName=models.CharField(max_length=50)
    Car=models.ForeignKey("Car",on_delete=models.CASCADE)

    class Meta:
        verbose_name="Bill"
        verbose_name_plural="Bills"




