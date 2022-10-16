import csv 

with open("C://Users//ASUS//Documens//sedri//data.csv","r") as csv_data:
    csv=csv.reader(csv_data,dialect=",")

    for row in csv_data:
        print(row)
