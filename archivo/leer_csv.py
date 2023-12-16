import csv

with open('archivo//datos.csv') as archivote:
    reader = csv.reader(archivote)
    for i in reader:
        print(i)