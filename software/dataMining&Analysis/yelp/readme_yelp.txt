yelp.py download data from yelp API.There are two parameter can be modified. The first one is "term" and three values,food,
gas station and entertainment, are used in our project. The second one is "radius_filter". 2000 is the radius we used in our
project,besides we also use 300 meters for food.For every element in the result dictionary,the key is property ID.The values 
is a dictionary which include the details of the search results.

yelp_details.py include all the  recodes in all search results and delete the redundance data.The output file is in same oder
with the yelp_details table in schema of database.

yelp_score.py calculate the food score, gas score and entertainment score of every property. 