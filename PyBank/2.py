import csv

# Initializing variables for totaling profit/loss by looping.
profit = 0
loss = 0
monthcount = 0
monthlychanges = []
firstmonth = 0 
difference_total = 0
monthdiffcount = 0
Greatest_Increase = 0
Greatest_Decrease = 0
Greatest_Increase_Month = 0
Greatest_Decrease_Month = 0

# opening up datafile as object.
with open("budget_data.csv", 'r', newline='') as myFile:
    reader = csv.reader(myFile, delimiter=',')
    next(reader)
    monthcount = 0
    for row in reader:
        monthcount += 1
    print(monthcount)    
            
