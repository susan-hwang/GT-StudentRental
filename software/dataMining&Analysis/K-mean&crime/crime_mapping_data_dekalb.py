from bs4 import BeautifulSoup
import urllib
import re
import csv
page = urllib.urlopen('http://www.crimemapping.com/DetailedReport.aspx?db=9/08/2015+00:00:00&de=9/30/2015+23:59:00&ccs=AR,AS,BU,DP,DR,DU,FR,HO,VT,RO,SX,TH,VA,VB,WE&xmin=-9431087.188707177&ymin=3972566.125166101&xmax=-9376052.528341923&ymax=3993433.4338879255')
soup = BeautifulSoup(page.read(), "html.parser")
# print soup.prettify()
# data = soup.find("div", {"class": "report"}).table.contents
# print soup.prettify()
count=0
# for row in soup.findAll("span")[3:]:
# 	if count < 5:
# 		print row.string,
# 		count = count+1
# 	else:
# 		count =0
# 		print "\n"
# 		print row.string,
# 		count = count+1

a = []
with open("9.1-30-3.csv", "wb") as f:
	writer = csv.writer(f)
	writer.writerow(('type', 'ID','location', 'police', 'time'))
	for row in soup.findAll("span")[3:]:
		if count < 5:
			a.append(row.string.encode('utf8'))
			count = count+1
		if count == 5: 
			writer.writerow(a)
			count = 0
			a = []
			

			

		# else:
		# 	count =0
		# 	writer.writerow("\n")
		# 	writer.writerow([row.string,])
		# 	count = count+1
    

f.close()

