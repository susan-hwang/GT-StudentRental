from django.db import models

class Property(models.Model):
    Place_ID=models.CharField(max_length=30,primary_key=True)
    Estate_Name=models.CharField(max_length=60)
    Altitude=models.FloatField()
    Longtitude=models.FloatField()
    Phone_Number=models.CharField(max_length=60,blank=True)
    Address=models.CharField(max_length=100,unique=True)
    City=models.CharField(max_length=30)
    Zipcode=models.CharField(max_length=5)
    Website=models.CharField(max_length=255,blank=True)
    Crime_Grade=models.DecimalField(max_digits=6,decimal_places=2)
    Yelp_Grade=models.DecimalField(max_digits=6,decimal_places=2)
    Grade=models.DecimalField(max_digits=6,decimal_places=2)


class Price(models.Model):
    Place_ID=models.ForeignKey('Property',on_delete=CASCADE)
    Bedroom=models.BigIntegerField(blank=True)
    Bathroom=models.DecimalField(max_digits=4,decimal_places=1,blank=True)
    BasePrice=models.DecimalField(max_digits=10,decimal_places=2)
    TopPrice=models.DecimalField(max_digits=10,decimal_places=2)

class Yelp_Details(models.Model):
    Name=models.CharField(max_length=100,primary_key=True)
    Address=models.CharField(max_length=100,primary_key=True)
    Category=models.CharField(max_lenfth=20,primary_key=True)
    Rating=models.DecimalField(max_digits=3,decimal_places=1)

class Yelp(models.Model):
    yelp=models.ForeignKey('Yelp_Details',primary_key=True)
    Place_ID=models.ForeignKey('Property',primary_key=True)
    IsWalk=models.BooleanField()
