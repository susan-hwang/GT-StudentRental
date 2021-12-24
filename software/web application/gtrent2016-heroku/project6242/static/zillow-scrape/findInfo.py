#r = open("sample.txt","r")
def findInfo(text,zipcode):
	zpid=""
	name=""
	typ=""
	address=""
	detailURL=""
	latitude=""
	longitude=""
	bath=""
	bed=""
	price=""
	area=""
	pet=""
	pos = 0
	grouped = text.find("grouped",0)
	findLatitude=text.find("latitude",pos)
	if findLatitude!=-1:
		pos=findLatitude+10
		while text[pos]!='"':
			latitude=latitude+text[pos]
			pos=pos+1
		latitude = latitude[:2]+"."+latitude[2:]
	findZip = text.find("zpid",pos)
	if findZip!=-1:
		pos=findZip+5
		while text[pos]!='"':
			zpid=zpid+text[pos]
			pos=pos+1
	findLongitude=text.find("longitude",pos)
	if findLongitude!=-1:
		pos=findLongitude+11
		while text[pos]!='"':
			longitude=longitude+text[pos]
			pos=pos+1
		longitude = longitude[:3]+"."+longitude[3:]
	findDetailURL = text.find("href",pos)
	if findDetailURL!=-1:
		detailURL="http://www.zillow.com"
		pos=findDetailURL+6
		while text[pos]!='"':
			detailURL=detailURL+text[pos]
			pos=pos+1
	findAdd = text.find("alt",pos)
	if findAdd!=-1:
		pos=findAdd+5
		while text[pos]!='"':
			address=address+text[pos]
			pos=pos+1
	findType = text.find("type-icon",pos)
	if findType!=-1:
		pos=findType+18
		while text[pos]!=' ':
			typ=typ+text[pos]
			pos=pos+1
	if grouped!=-1:
		findName = text.rfind("title")
		pos = findName +8
		while text[pos]!='"':
			name = name+text[pos]
			pos = pos +1
	else:
		name = address[:address.find(",")-1]
	return name+"\t"+latitude+"\t"+longitude+"\t"+address+"\t"+str(zipcode)+"\t"+typ+"\t"+detailURL+"\n"




