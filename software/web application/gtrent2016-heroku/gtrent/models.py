from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Property(models.Model):
    Place_ID=models.CharField(max_length=30,primary_key=True,default="001")
    Estate_Name=models.CharField(max_length=60, null=True)
    Altitude=models.FloatField(default=33.0)
    Longtitude=models.FloatField(default=33.0)
    Phone_Number=models.CharField(max_length=60,null=True)
    Address=models.CharField(max_length=100,null=True)
    City=models.CharField(max_length=30,null=True)
    Zipcode=models.CharField(max_length=5,null=True)
    Website=models.CharField(max_length=255,null=True)
    Crime_Grade=models.DecimalField(max_digits=6,decimal_places=2, null=True)
    Food_Grade=models.DecimalField(max_digits=6,decimal_places=2, null=True)
    Gas_Grade=models.DecimalField(max_digits=6,decimal_places=2, null=True)
    Entertainment_Grade=models.DecimalField(max_digits=6,decimal_places=2, null=True)
#    Yelp_Grade=models.DecimalField(max_digits=6,decimal_places=2, null=True)
#    Grade=models.DecimalField(max_digits=6,decimal_places=2, null=True)
    Type=models.CharField(max_length=40, null=True)
    drivingTime=models.IntegerField(null=True)
    walkingTime=models.IntegerField(null=True)
    transitTime=models.IntegerField(null=True)
    cluster=models.IntegerField(null=True)

class Price(models.Model):
    ID=models.IntegerField(primary_key=True, default=0)
    Place_ID=models.CharField(max_length=30,default="001", null=True)
    Bedroom=models.BigIntegerField(null=True)
    Bathroom=models.DecimalField(max_digits=4,decimal_places=1,null=True)
    SquareFeet=models.FloatField(default=300, null=True)
    BasePrice=models.DecimalField(max_digits=10,decimal_places=2, null=True)
#    TopPrice=models.DecimalField(max_digits=10,decimal_places=2, null=True)

class Yelp_Details(models.Model):
    Name=models.CharField(max_length=100,primary_key=True, default="111")
    Address=models.CharField(max_length=100, null=True)
    Category=models.CharField(max_length=20, null=True)
    Rating=models.DecimalField(max_digits=3,decimal_places=1)

class Yelp(models.Model):
    yelp=models.ForeignKey('Yelp_Details',primary_key=True,default = "111")
    Place_ID=models.ForeignKey('Property', default="001")
    IsWalk=models.BooleanField(default=True)

