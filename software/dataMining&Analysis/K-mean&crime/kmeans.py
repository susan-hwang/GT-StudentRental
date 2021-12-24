
import json
import csv
from geopy.distance import great_circle
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist, pdist
from sklearn.metrics import silhouette_score

from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import numpy as np

import time

# dt_trans = np.random.randn(100, 5)

ofile  = open('cluster.csv', "wb")
writer = csv.writer(ofile, delimiter=',')

f1 = json.loads(open('rentalList_refined_addTime_addCrimeScoreToGT.json').read())
GT_position = [33.778463, -84.398881]
ID=[]
data = []
for line in f1:
	position = []
	#print line["Longitude"]
	lon = float(line["Longitude"])
	lat = float(line["Latitude"])
	position.append(lat)
	position.append(lon)
	distance = float(great_circle(GT_position, position).miles)
	data.append(distance)
	ID.append(line["ID"])

	# drivingtime = int(line["drivingTime"])
	# data.append(drivingtime)
	# walkingtime = int(line["walkingTime"])
	# data.append(walkingtime)
	# transittime = int(line["transitTime"])
	# data.append(transittime )

	# crimescore = float(line["nomalized_crime_score"])
	# data.append(crimescore)
	# yelpscore = 
	
dt_trans=np.array(data).reshape(1097,1)

#print dt_trans


K = range(10,11)
KM = [KMeans(n_clusters=k).fit(dt_trans) for k in K]
centroids = [k.cluster_centers_ for k in KM]

D_k = [cdist(dt_trans, cent, 'euclidean') for cent in centroids]
cIdx = [np.argmin(D,axis=1) for D in D_k]
np.set_printoptions(threshold=np.nan)
cluster = cIdx
#print ID
#print cluster

for index,item in enumerate(cluster[0]):
	#print index+1,item
	result = [index+1,item]
	writer.writerow(result)
#result = np.dstack((ID,cluster))
#print result

dist = [np.min(D,axis=1) for D in D_k]
avgWithinSS = [sum(d)/dt_trans.shape[0] for d in dist]

# Total with-in sum of square
wcss = [sum(d**2) for d in dist]
tss = sum(pdist(dt_trans)**2)/dt_trans.shape[0]
bss = tss-wcss

kIdx = 10-1

# elbow curve
# with PdfPages('elbow_method_result1.pdf') as pdf:

# 	fig = plt.figure()
# 	ax = fig.add_subplot(111)
# 	ax.plot(K, avgWithinSS, 'b*-')
# 	ax.plot(K[kIdx], avgWithinSS[kIdx], marker='o', markersize=12, 
# 	markeredgewidth=2, markeredgecolor='r', markerfacecolor='None')
# 	plt.grid(True)
# 	plt.xlabel('Number of clusters')
# 	plt.ylabel('Average within-cluster sum of squares')
# 	plt.title('Elbow for KMeans clustering')
# 	pdf.savefig()
# 	plt.close()

# with PdfPages('elbow_method_result2.pdf') as pdf:
# 	fig = plt.figure()
# 	ax = fig.add_subplot(111)
# 	ax.plot(K, bss/tss*100, 'b*-')
# 	plt.grid(True)
# 	plt.xlabel('Number of clusters')
# 	plt.ylabel('Percentage of variance explained')
# 	plt.title('Elbow for KMeans clustering')

# 	pdf.savefig()  # saves the current figure into a pdf page
# 	plt.close()

ofile.close()
