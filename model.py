from geopy.distance import geodesic
import csv 
from datetime import datetime 
from datetime import timedelta 

# csv file name 
filename = "cityData.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 

# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
    
    # extracting field names through first row 
    fields = next(csvreader) 

    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row) 

    # get total number of rows 
    #print("Total no. of rows: %d"%(csvreader.line_num)) 

# printing the field names 
#print('Field names are:' + ', '.join(field for field in fields)) 

origin = input("Enter origin city: ") 
destination = input("Enter destination city: ")
date = input("Enter date of dispatch(YYYY-DD-MM): ")

#Load data of given origin and destination
for i in range(len(rows)):
    if (rows[i][0] == origin):
        locOrigin = eval(rows[i][1])
    if (rows[i][0] == destination):
        locDest = eval(rows[i][1])
    if (rows[i][0] == origin):
        stateOrigin = rows[i][2]
    if (rows[i][0] == destination):
        stateDest = rows[i][2]
    if (rows[i][0] == origin):
        avgSpeedOrigin = rows[i][3]
    if (rows[i][0] == destination):
        avgSpeedDest = rows[i][3]
        
dist = geodesic(locOrigin, locDest).miles

speed = 0
for i in range(len(rows)):
    speed+= float(rows[i][3])

averageSpeed = speed/len(rows)

if((stateOrigin == stateDest) or (dist<200)):
    eta = dist/((float(avgSpeedOrigin)+float(avgSpeedDest))/2)
else:
    eta = ((dist-200)/averageSpeed) + (100/float(avgSpeedOrigin)) + (100/float(avgSpeedDest))

if (eta>12):
    eta = eta + (12*round(eta/24))
eta = int(eta)

Begindate = datetime.strptime(date, "%Y-%d-%m")
Enddate = Begindate + timedelta(hours=eta)

def Main():
    print('Distance between', origin[0].upper() + origin[1:] , 'and' ,destination[0].upper() + destination[1:] , 'is', int(dist),'miles')
    print('You may expect your package by:',Enddate)

if __name__=="__main__": 
    Main() 

