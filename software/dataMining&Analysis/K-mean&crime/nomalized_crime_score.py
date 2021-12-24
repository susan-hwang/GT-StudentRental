import csv

ofile  = open('nomalized_crime_score.csv', "wb")
writer = csv.writer(ofile, delimiter=',')

f = open("crime_score.csv")
csvfile = csv.reader(f)
for line in csvfile:
	writer.writerows([x.split(',') for x in line])

ofile.close()


f2 = open("nomalized_crime_score.csv")
csvfile2 = csv.reader(f2)

for line in csvfile2:
	
	normalized_score = ((float(line[1]))+1.0691618775)*40/1.0691618775+60
	#normalized_score = (((float(line[1]))/18.3290313)+1)*100
	print normalized_score


