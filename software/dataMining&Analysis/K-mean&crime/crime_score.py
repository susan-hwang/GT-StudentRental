import json
import csv
from geopy.distance import great_circle

ofile  = open('crime_score.csv', "wb")
writer = csv.writer(ofile, delimiter=',')

f1 = json.loads(open('rentalList_refined_addTimeToGT.json').read())

count = 0
maxi = 0
total = 0
for line in f1:
	#if count<5:
		data1 = []
		#print line["Longitude"]
		lon1 = float(line["Longitude"])
		lat1 = float(line["Latitude"])
		data1.append(lat1)
		data1.append(lon1)
		#print data1

		f2 = open("final_dekalb_data.csv")
		f3 = open("cleaned-2015.8-2016-Crime-Data-csv.csv")
		csvfile2 = csv.reader(f2)
		csvfile3 = csv.reader(f3)
		csvfile2.next()
		csvfile3.next()

		
		for line2 in csvfile2:
			data2 = []
			lon2 = float(line2[7])
			lat2 = float(line2[6])
			data2.append(lat2)
			data2.append(lon2)

			impact = 0
			total_impact = 0
			distance = (great_circle(data1, data2).miles)
			if distance < 0.15:
				impact = -0.14/0.15* distance
				total_impact = impact+ total_impact


		
		for line3 in csvfile3:
			data3 = []
			lon3 = float(line3[4])
			lat3 = float(line3[5])
			data3.append(lat3)
			data3.append(lon3)
		

			distance = (great_circle(data1, data3).miles)
			if distance < 0.15:
				impact = -0.14/0.15* distance
				total_impact = impact+ total_impact

		content = [ line["Name"]+ "," + str(total_impact)]
		writer.writerow(content)

		total = total + total_impact

		if total_impact < maxi:
			maxi = total_impact

	
		count = count +1

		f2.close()
		f3.close()

writer.writerow([str(maxi)])

mean = total/count
writer.writerow([str(mean)])

ofile.close()

			
