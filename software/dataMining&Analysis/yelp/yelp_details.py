#yelp_details
import json
def main():
    yelp_detail=[]

#----------------food--------------------------------------#
    file1=open("./yelp-food-2000.json")
    food=json.load(file1)
    for pro1 in food:
        #print(food[pro1])
        for ele1 in food[pro1]["businesses"]:
            #print(food[pro1]["businesses"][ele1])
            #a=str(ele1)+"|"+str(food[pro1]["businesses"][ele1]["location"])
            a={"Name":ele1,"Address":food[pro1]["businesses"][ele1]["location"],\
               "Rating":food[pro1]["businesses"][ele1]["rating"],"Category":"food"}
            if a not in yelp_detail:
                yelp_detail.append(a)

#-----------------entertainment----------------------------#
    file2=open("./yelp-Entertainment-2000.json")
    entertain=json.load(file2)
    for pro2 in entertain:
        for ele2 in entertain[pro2]["businesses"]:
            a={"Name":ele2,"Address":entertain[pro2]["businesses"][ele2]["location"],\
               "Rating":entertain[pro2]["businesses"][ele2]["rating"],"Category":"entertaiment"}
            if a not in yelp_detail:
                yelp_detail.append(a)
                
#------------------gas-------------------------------------#

    file3=open("./yelp-gas-2000.json")
    gas=json.load(file3)
    for pro1 in gas:
        for ele1 in gas[pro1]["businesses"]:
            a={"Name":ele1,"Address":gas[pro1]["businesses"][ele1]["location"],\
               "Rating":gas[pro1]["businesses"][ele1]["rating"],"Category":"gas"}
            if a not in yelp_detail:
                yelp_detail.append(a)
    
    json.dump(yelp_detail,open("Yelp_Details.json","w"))
                
main()
