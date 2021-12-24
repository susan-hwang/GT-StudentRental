from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import json
import time
def main():
    file1=open("rentalList_refined_addTimeToGT.tsv")
    #file2=open("yelp-food.csv","w")
    auth=Oauth1Authenticator(
        consumer_key="o_aIg7was3GmovP3qevfgA",
        consumer_secret="s6Esfj24UWGfcys1SW_AjBq0ts0",
        token="cCswiRCroK79F-3rpuswZTPXHe7YoFQY",
        token_secret="TOzzZTd5ZwrTN5RExDUiv0fNBf8"
        )
    client=Client(auth)
    params={
        'term':"gas station",
        'radius_filter':2000
        }
    line1=file1.readline().strip("\n")
    #file2.write("property,foodtotal,")
    data2={}
    n=0
    while True:
        line1=file1.readline().strip("\n")
        if line1=="":
            break
        else:
            s1=line1.split("\t")
            #data2.append({})
            data2[s1[0]]={}
            #n1=len(data2)-1
            #data2[n1]["property"]=s1[0]
            response=client.search_by_coordinates(float(s1[2]),float(s1[3]),**params)
            n=n+1
            if n==200:
                time.sleep(100)
                n=0
            #print(response.total)
            data2[s1[0]]["total"]=response.total
            #print(response.total)
            data2[s1[0]]["businesses"]={}
            i=0
            for i in range(len(response.businesses)):
                #print(i)
                #data2[s1[0]]["businesses"].append({})
                #print(response.businesses[i].name)
                data2[s1[0]]["businesses"][response.businesses[i].name]={}
                #n2=len(data2[n1]["businesses"])-1
                #data2[n1]["businesses"][n2]["name"]=response.businesses[i].name
                #print(response.businesses[i].rating)
                data2[s1[0]]["businesses"][response.businesses[i].name]["location"]=response.businesses[i].location.address
                data2[s1[0]]["businesses"][response.businesses[i].name]["rating"]=response.businesses[i].rating
    #print(type(data2))
    json.dump(data2,open("yelp-gas-2000.json","w"))
            
main()            
