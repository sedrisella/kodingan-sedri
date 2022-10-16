import csv

#users = open("data.csv","r")
#file:data.csv
import csv 

with open("data.csv","r") as filecsv:
    datafile =csv.reader(filecsv)
    for data in datafile:
        print(data)
