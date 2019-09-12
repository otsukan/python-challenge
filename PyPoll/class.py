import csv
import os

os.path.join("file.csv")

with open("file.csv", 'w' ,newline='') as ya:
    variable = csv.writer( ya, delimiter=',')

    header = ["Name", "Age", "Birthdate"]
    information = ["Nathan Otsuka", "28", "12/27/1990"]

    variable.writerow(header)
    variable.writerow(information)

