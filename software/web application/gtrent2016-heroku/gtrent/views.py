from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
import json

def index(request):
        if request.is_ajax():
                # get data from json
                commutingStyle= request.GET.get('commutingStyle')
                commutingTime = [float(request.GET.get('commutingTimeMin'))*60.0, float(request.GET.get('commutingTimeMax'))*60.0]
                beds = int(request.GET.get('bed'))
                baths = float(request.GET.get('bath'))
                priceRange = [float(request.GET.get('priceMin')), float(request.GET.get('priceMax'))]
                types = [request.GET.get('Apartment'), request.GET.get('House'), request.GET.get('Condo'), request.GET.get('Townhouse')]
                lifestyle = [int(request.GET.get('Food') == "true"), int(request.GET.get('Gas') == "true"), int(request.GET.get('Entertainment') == "true")]
                
                # return json data
                property = []
                if commutingStyle == "driving":
                        property = Property.objects.filter(drivingTime__gte = commutingTime[0]).filter(drivingTime__lte = commutingTime[1])
                if commutingStyle == "walking":
                        property = Property.objects.filter(walkingTime__gte = commutingTime[0]).filter(walkingTime__lte = commutingTime[1])
                if commutingStyle == "transit":
                        property = Property.objects.filter(transitTime__gte = commutingTime[0]).filter(transitTime__lte = commutingTime[1])
                
                typelist = ['Apartment', 'House', 'Condo', 'Townhouse']
                typeincluded = []
                for i in range(0, 4):
                        if types[i] == "true":
                                typeincluded.append(typelist[i])
                property_list = []
                for check in property:
                        if check.Type in typeincluded:
                                average_score = (float(check.Food_Grade)*lifestyle[0] + float(check.Gas_Grade)*lifestyle[1] + float(check.Entertainment_Grade)*lifestyle[2])/float(lifestyle[0]+lifestyle[1]+lifestyle[2])
                                property_list.append(check)
                
                
                zillow = Price.objects.filter(Bedroom = beds).filter(Bathroom = baths).filter(BasePrice__gte = priceRange[0]).filter(BasePrice__lte = priceRange[1])
                json_property = []
                for check in property_list:
                        for id in zillow:
                                if check.Place_ID == id.Place_ID:
                                        fplan = []
                                        byID = Price.objects.filter(Place_ID = check.Place_ID)
                                        for oneplan in byID:
                                                fplan.append({"bed":oneplan.Bedroom,
                                                              "bath":float(oneplan.Bathroom),
                                                              "price":float(oneplan.BasePrice),
                                                              "sqft":float(oneplan.SquareFeet)})
                                        json_property.append({"commutingStyle":commutingStyle,
                                                              "drivingTime":float(check.drivingTime),
                                                              "walkingTime":float(check.walkingTime),
                                                              "transitTime":float(check.transitTime),
                                                              "name":check.Estate_Name,
                                                              "address":check.Address,
                                                              "lat":float(check.Altitude),
                                                              "lon":float(check.Longtitude),
                                                              "webSite":check.Website,
                                                              "zipCode":check.Zipcode,
                                                              "floorPlans":fplan,
                                                              "propertyType":check.Type,
                                                              "crimeScore":float(check.Crime_Grade),
                                                              "foodScore":float(check.Food_Grade),
                                                              "gasScore":float(check.Gas_Grade),
                                                              "entertainmentScore":float(check.Entertainment_Grade),
                                                              "averageScore":80,
                                                              "cluster":check.cluster})
                                        break;
                
                return HttpResponse(json.dumps(json_property), content_type='application/json')

        return render(request, 'gtrent/index.html')

# Create your views here.
