
from urllib2 import Request, urlopen
import csv
#import getZip as gz

w = open("rentalList_refined_addTimeToGT-transit.tsv", "wb")
gt="33.778016,-84.399205"
def findRouteTime(origins,destinations,mode):
	#parameter
	parameter = ''
	paraDic = {
	'key' : "AIzaSyDTYfIgWA-BGuC1obnERZv8rm1p-Jnx6oY",  
	'origins' : origins,	
	'destinations' : destinations,	
	#'departure_time': "now",
	'mode':mode
	}
	for key in paraDic:
		parameter = parameter+key+'='+paraDic[key]+'&'
	#print parameter

	request = Request("https://maps.googleapis.com/maps/api/distancematrix/json?"+parameter)
	text = urlopen(request).read()
	pos = 0
	temp = ''
	#print text

	while pos < len(text)-1:
		searchTime = text.find('duration',pos)
		if searchTime != -1:
			searchTime = text.find('value',searchTime+9)
			i = searchTime + 9
			while text[i] != '\n':
				temp = temp + text[i]
				i = i+1
			pos = i
			break
		else:
			return 0
	return int(temp)



with open("rentalList_refined.tsv","rU") as r:
    tsvin = csv.reader(r, dialect=csv.excel_tab)
    csvout = csv.writer(w,dialect=csv.excel_tab)
    count = 0
    for row in tsvin:
    	count = count+1
    	print count
    	if count==1:
    		row.append("transitTime")
    		csvout.writerow(row)
    	else:
    		transitTime1 = findRouteTime(gt,row[1]+','+row[2],"transit")
    		transitTime2 = findRouteTime(row[1]+','+row[2],gt,"transit")
    		row.append((transitTime1+transitTime2)/2);
    		csvout.writerow(row)
    print "end"
    w.close()
    r.close()


