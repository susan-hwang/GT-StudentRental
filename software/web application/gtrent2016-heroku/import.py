import psycopg2
import sys
import csv


con = None

file = open("../rentalList_Time_crime_scorefinal.tsv", "rU")
reader = csv.DictReader(file, delimiter='\t')

try:
     
    con = psycopg2.connect(database='dbgtrent', user='qige') 
    cur = con.cursor()
    for row in reader:
        value = "'" + row["ID"] + "','" + row["Name"] + "'," + str(row["Latitude"]) + "," + str(row["Longitude"]) + ",'"  + "000-000-0000" + "','" + row["Address"] + "','Atlanta','" + row["Zipcode"] + "','" + row["Website"] + "'," + str(row["nomalized_crime_score"]) + "," + str(row["foodscore"]) + "," + str(row["entertainmentscore"]) + ",'" + row["Type"] + "'," + str(row["drivingTime"]) + "," + str(row["transitTime"]) + "," + str(row["walkingTime"]) + "," + str(row["gasscore"]) + "," + str(row["clusters"])
        cur.execute("INSERT INTO gtrent_property VALUES("+value+")")

    con.commit()
    
except psycopg2.DatabaseError, e:
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()
