#yelp grades
import json
def main():
    file1=open("./yelp-food-2000.json")
    file2=open("./yelp-Entertainment-2000.json")
    file3=open("./yelp-gas-2000.json")
    food=json.load(file1)
    entertain=json.load(file2)
    gas=json.load(file3)
    foodmax=0
    entertainmax=0
    gasmax=0
    proper=[]
    #properenter=[]
    #propergas=[]
    foodscore=[]

#------------------------------find max----------------------------------------#
    for ele1 in food:
        ratingsum=0
        proper.append(ele1)
        for name in food[ele1]["businesses"]:
            ratingsum=ratingsum+float(food[ele1]["businesses"][name]["rating"])/5
        foodscore.append(ratingsum)
        if ratingsum>foodmax:
            foodmax=ratingsum
    entertainscore=[0 for i in range(len(proper))]
    for ele1 in entertain:
        ratingsum=0
        #properenter.append(ele1)
        for name in entertain[ele1]["businesses"]:
            ratingsum=ratingsum+float(entertain[ele1]["businesses"][name]["rating"])/5
        n=proper.index(ele1)
        entertainscore[n]=ratingsum
        if ratingsum>entertainmax:
            entertainmax=ratingsum
    gasscore=[0 for i in range(len(proper))]
    for ele1 in gas:
        n=proper.index(ele1)
        gasscore[n]=gas[ele1]["total"]
        if float(gas[ele1]["total"])>gasmax:
            gasmax=float(gas[ele1]["total"])
#---------------------------calculate score------------------------------------#
    print gasmax
    for i in range(len(proper)):
        foodscore[i]=100.0*foodscore[i]/foodmax
        entertainscore[i]=100.0*entertainscore[i]/entertainmax
        #print gasscore[i]
        gasscore[i]=100.0*gasscore[i]/gasmax

    score=[]
    #for i in range(len(proper)):
    #    score.append((0.5*foodscore[i]+0.3*entertainscore[i]+0.2*gasscore[i])*100)
    #result=[]
    
    #for i in range(len(proper)):
    #    a={"property":proper[i],"score":score[i]}
    #    result.append(a)
    #json.dump(result,open("yelp_score.json","w"))
    kmeans=[]
    file4=open("./cluster.csv")
    line4=file4.readline().strip("\n")
    while True:
        line4=file4.readline().strip("\n")
        if line4=="":
            break
        else:
            s4=line4.split(",")
        #print s4[1]
            kmeans.append(s4[1])
    file5=open("./rentalList_refined_addTime_addCrimeScoreToGT.json")
    file6=open("rentalList_Time_crime_score.tsv","w")
    file6.write("ID\tName\tLatitude\tLongitude\tAddress\tZipcode\tType\tWebsite\tdrivingTime\twalkingTime\ttransitTime\tnomalized_crime_score\tfoodscore\tgasscore\tentertainmentscore\n")
    #print len(foodscore)
    #print len(crime)
    crime=json.load(file5)
    #print len(crime)
    #for ele1 in crime:
    for i in range(1097):
        #print crime[i]["ID"]
        #print crime[i]["ID"]
        #print type(crime[i]["ID"])
        #if type(crime[i]["ID"])=="int":
        #    print aaaaaaaaa
        #    pass
        #else:
        #    print crime[i]["ID"]
        n=proper.index(unicode(str(crime[i]["ID"]),"utf-8"))
        #print type(proper[0])
        #print type(crime[i]["ID"])
        crime[i]["foodscore"]=foodscore[n]
        crime[i]["gasscore"]=gasscore[n]
        crime[i]["entertaimentsocre"]=entertainscore[n]
        if crime[i]["Type"]=="Apartments":
            crime[i]["Type"]="Apartment"
        elif crime[i]["Type"]=="Condos":
            crime[i]["Type"]="Condo"
        del crime[i]["address2"]
        del crime[i]["raw_crime_score"]
        #ele1["foodscore"]=foodscore[ele1["ID"]]
        #ele1["gasscore"]=gasscore[ele1["ID"]]
        #ele1["entertaimentsocre"]=entertainscore[ele1["ID"]]
        #del ele1["address2"]
        #del ele1["raw_crime_score"]
        a='\t'.join([str(crime[i]["ID"]),crime[i]["Name"],str(crime[i]["Latitude"]),str(crime[i]["Longitude"]),\
                     crime[i]["Address"],str(crime[i]["Zipcode"]),crime[i]["Type"],crime[i]["Website"],\
                     str(crime[i]["drivingTime"]),str(crime[i]["walkingTime"]),str(crime[i]["transitTime"]),\
                     str(crime[i]["nomalized_crime_score"]),str(crime[i]["foodscore"]),str(crime[i]["gasscore"]),\
                     str(crime[i]["entertaimentsocre"])])
        file6.write(a+"\n")
    json.dump(crime,open("rentalList_Time_crime_score.json","w"))
    
    
    
            
        
        
main()
        
    
        
        
    
