Atlanta crime data are downloaded from Atlanta Police Department "http://www.atlantapd.org/crimedatadownloads.aspx".
DeKalb county crime data are scraped from www.crimemapping.com with the file "crime_mapping_data_dekalb.py".
All the data are cleaned with google OpenRefine.
Crime scores of every property are calculated and nomalized using the file"crime_score.py" and "nomalized_crime_score.py".

"kmeans.py" used “latitude”, “longitude”, “distance to GT”, “crime score”,“gas score”, “food score”and “entertainment score” as attributes to cluster properties and evaluate with elbow method.
"cluster_plot.py" draws the scatter plot of clustering result.
