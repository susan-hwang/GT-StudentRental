import urllib2
import findInfo as fi
import json
ww = open("sample22.txt","w")
def findApartmentPrice(id,text):
	#print id
	priceMap=[]
	findList=text.find('id="units-list_available',0)
	if findList!=-1:
		findBed = text.find('data-bedroom',findList)
		findNum1 = text.find(">",text.find("span",text.find("matching-units",0)))
		findNum2 = text.find("<",findNum1)
		Num = int(text[findNum1+1:findNum2])
		#print id,Num,text[findNum1-15:findNum2+5]
		count =0
		while findBed!=-1 and count<Num:
			count = count +1
			floorPlan={}
			bed = text[findBed+14]
			#print [findBed,bed,text[findBed:findBed+30]]
			findPrice1=text.find('>$',findBed)
			findPrice2=text.find('<',findPrice1)
			price = text[findPrice1+2:findPrice2]
			price = price.replace(",","")
			price = price.replace("+","")
			findBath1=text.find('building-units-baths',findPrice2)
			findBath2=text.find('ba',findBath1+22)
			bath = text[findBath1+22:findBath2]
			#print text[findBath1-5:findBath2+5],bath
			findSqft1=text.find('>',text.find('building-units-sqft',findBath2))
			findSqft2=text.find('sqft',findSqft1)
			sqft = text[findSqft1+1:findSqft2]
			sqft = sqft.replace(",","")
			sqft = sqft.replace("-","0")
			bath = bath.replace("-","0")
			floorPlan["ID"]=id
			floorPlan["bed"]=int(bed)
			floorPlan["bath"]=float(bath)
			floorPlan["price"]=int(price)
			floorPlan["sqft"]=int(sqft)
			#print floorPlan
			priceMap.append(floorPlan)
			findBed = text.find('data-bedroom',findSqft2)
	else:
		#print id+" something wrong!"
		return findHousePrice(id,text)
	return priceMap
def findHousePrice(id,text):
	priceMap=[]
	floorPlan={}
	bed=""
	bath=""
	sqft=""
	price=""
	findList=text.find('zsg-content-header addr',0)
	if findList!=-1:
		findBed1=text.find("addr_bbs",findList)
		findBed2=min(text.find("bed",findBed1),text.find("<",findBed1))
		bed = text[findBed1+10:findBed2]
		if bed=="Studio":
			bed="0"
		findBath1=text.find("addr_bbs",findBed2)
		findBath2=text.find("bath",findBath1)
		bath = text[findBath1+10:findBath2]
		findSqft1=text.find("addr_bbs",findBath2)
		findSqft2=text.find("sqft",findSqft1)
		sqft = text[findSqft1+10:findSqft2]
	else:
		print id+" something wrong!"
		return []

	findList=text.find('main-row  home-summary-row',0)
	if findList!=-1:
		findPrice1=text.find('$',findList)
		findPrice2=text.find('<',findPrice1)
		price = text[findPrice1+1:findPrice2]
	else:
		print id+" something wrong!"
		return []
	price=price.replace(",","")
	price=price.replace("+","")
	sqft = sqft.replace(",","")
	sqft = sqft.replace("-","0")
	bath = bath.replace("-","0")
	floorPlan["ID"]=id
	floorPlan["bed"]=int(bed)
	floorPlan["bath"]=float(bath)
	floorPlan["price"]=int(price)
	floorPlan["sqft"]=int(sqft)
	#print floorPlan
	priceMap.append(floorPlan)
	return priceMap



def getRentals(Map):

	response = urllib2.urlopen(Map["Website"])
	page_text = response.read()
	ww.write(page_text)
	print Map["ID"]
	if Map['Type']=="Apartments":
		return findApartmentPrice(Map['ID'],page_text)
	if Map['Type']=="House":
		return findHousePrice(Map['ID'],page_text)
	if Map['Type']=="Condo":
		return findApartmentPrice(Map['ID'],page_text)
	if Map['Type']=="Townhouse":
		return findHousePrice(Map['ID'],page_text)

priceMap=[]
with open("rentalList_refined_addTimeToGT.json",'r') as rentalList:
	rentals = json.load(rentalList)
	count=0
	for Map in rentals:
		count=count+1
		if count!=27:
			pass
		priceMap=priceMap+getRentals(Map)

#print priceMap
with open('priceList.json',"w") as w:
	json.dump(priceMap,w)
	w.close()
	


