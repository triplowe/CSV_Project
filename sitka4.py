import csv
import matplotlib.pyplot as plt
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file,delimiter=",")

header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)

#testing to convert date from string
#mydate = datetime.strptime("2018-07-01", "%Y-%m-%d")

highs = []
lows = []
dates = []

for row in csv_file:
    try:
        theDate = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"Missing Data for {theDate}")
    else:
        dates.append(theDate)
        lows.append(int(row[5]))
        highs.append(int(row[4]))

#print(highs)
#print(dates)
#print(lows)

'''
fig = plt.figure()

plt.title("Daily high temperatures, July 2018", fontsize = 16)
plt.xlabel("", fontsize = 12)
plt.ylabel("Temperatures (F)", fontsize = 12)
plt.tick_params(axis = "both", which = "major", labelsize = 12)

plt.plot(dates, highs, c = "red", alpha = 0.5)
plt.plot(dates, lows, c = "blue", alpha = 0.5)

plt.fill_between(dates, highs, lows, facecolor = "blue", alpha = 0.1)

fig.autofmt_xdate()

plt.show()

#plt.subplot(row,col,index)
plt.subplot(2,1,1)
plt.plot(dates,highs,c="red")
plt.title("Highs")

plt.subplot(2,1,2)
plt.plot(dates,lows,c="blue")
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka Alaska")

plt.show()
'''