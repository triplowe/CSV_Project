import csv
from typing import Counter
import matplotlib.pyplot as plt
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")
open_file2 = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file,delimiter=",")
csv_file2 = csv.reader(open_file2,delimiter=",")

header_row = next(csv_file)
header_row2 = next(csv_file2)

'''
Finding the headers
print(type(header_row))
print(type(header_row2))
'''

for index, column_header in enumerate(header_row):
    #print(index, column_header)
    if column_header == "TMAX":
        TMAX = index
    if column_header == "TMIN":
        TMIN = index
    if column_header == "DATE":
        DATE = index
    if column_header == "NAME":
        STATION = index

for index, column_header in enumerate(header_row2):
    #print(index, column_header)
    if column_header == "TMAX":
        TMAX2 = index
    if column_header == "TMIN":
        TMIN2 = index
    if column_header == "DATE":
        DATE2 = index
    if column_header == "NAME":
        STATION2 = index
'''
Cheching to make sure my indexes are correct
print(type(TMAX), TMAX)
print(type(TMIN), TMIN)
print(type(DATE), DATE)
print(type(TMAX2), TMAX2)
print(type(TMIN2), TMIN2)
print(type(DATE2), DATE)
print(type(STATION), STATION)
print(type(STATION2), STATION2)
'''

#testing to convert date from string
#mydate = datetime.strptime("2018-07-01", "%Y-%m-%d")

highs = []
lows = []
dates = []

highs2 = []
lows2 = []
dates2 = []

for row in csv_file:
    try:
        theDate = datetime.strptime(row[DATE], "%Y-%m-%d")
        high = int(row[TMAX])
        low = int(row[TMIN])
        Station_name = row[STATION]
    except ValueError:
        print(f"Missing Data for {theDate}")
    else:
        dates.append(theDate)
        lows.append(int(row[TMAX]))
        highs.append(int(row[TMIN]))

for row in csv_file2:
    try:
        theDate2 = datetime.strptime(row[DATE2], "%Y-%m-%d")
        high = int(row[TMAX2])
        low = int(row[TMIN2])
        Station_name2 = row[STATION2]
    except ValueError:
        print(f"Missing Data for {theDate2}")
    else:
        dates2.append(theDate2)
        lows2.append(int(row[TMAX2]))
        highs2.append(int(row[TMIN2]))


#plt.subplot(row,col,index)
fig = plt.figure()

plt.subplot(2,1,1)
plt.plot(dates2,highs2,c="blue", alpha = 0.5)
plt.plot(dates2, lows2, c="red", alpha = 0.5)
plt.fill_between(dates2, highs2, lows2, facecolor = "blue", alpha = 0.1)
plt.title(Station_name2)
fig.autofmt_xdate()

plt.subplot(2,1,2)
plt.plot(dates,highs,c="blue", alpha = 0.5)
plt.plot(dates, lows, c="red", alpha = 0.5)
plt.fill_between(dates, highs, lows, facecolor = "blue", alpha = 0.1)
plt.title(Station_name)
fig.autofmt_xdate()



plt.suptitle(f"Temperature comparison between {Station_name} and {Station_name2}")

plt.show()

