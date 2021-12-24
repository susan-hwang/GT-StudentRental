import urllib2
import findInfo as fi
w = open("rentalList.txt","w")
def getRentals(zipcode):
	rentalList=""
	i=0
	while True:
		i=i+1
		response = urllib2.urlopen("http://www.zillow.com/homes/for_rent/GA-"+str(zipcode)+"/house,condo,apartment_duplex,mobile,townhouse_type/"+str(i)+"_p/")
		page_text = response.read()
		#w.write(page_text)
		articleTimes = page_text.count("article")
		print i
		#print articleTimes
		if articleTimes ==1:
			break
		findArticle = page_text.find("article",0)
		for j in range((articleTimes-1)/2):
			findArticle = page_text.find("article",findArticle+5)
			beg=findArticle
			findArticle = page_text.find("article",findArticle+5)
			end=findArticle
			rentalList=rentalList+fi.findInfo(page_text[beg:end],zipcode)
	return rentalList
w.write(getRentals(30339))


