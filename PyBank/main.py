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

# opening up datafile as object.
with open("budget_data.csv", newline='') as myFile:
    
    # setting datafile as csv reader object.
    reader = csv.reader(myFile, delimiter=',')
    
    # skip the first row/header
    next(reader)
    
    for row in reader:
        
        # calculate total months
        monthcount += 1    
        
        # fill list full of monthly changes
        monthlychange = int(row[1]) - firstmonth
        monthlychanges.append(monthlychange)   
        firstmonth = int(row[1])
        
        # calculate total profit
        if int(row[1]) > 0:
            profit += int(row[1])
        
        # calculate total loss
        elif int(row[1]) < 0:
            loss += int(row[1])
    
    # calculate net profit.
    net_profit = profit + loss
    
    # take first entry out of monthlychanges
    monthlychanges.pop(0)
    
    for difference in monthlychanges:
       
        # sum the total of all the monthly changes
        difference_total += int(difference)
        
        # calculate # fields in monthlychanges
        monthdiffcount += 1
        
        # Calculate Greatest Monthly Increase in Earnings
        if int(difference) > Greatest_Increase:
            Greatest_Increase = int(difference)
        
        # Calculate Greastest Monthly Decrease in Earnings
        elif int(difference) < Greatest_Decrease:
            Greatest_Decrease = int(difference)
    
    # calculate average monthly change
    average_monthly_change = int(difference_total)/int(monthdiffcount)
    
# printing the results/analysis of our dataset
print(f"Total Months: {monthcount}")
print(f"Total: ${net_profit:,.0f}".replace('$-','-$'))
print(f"Average Change: ${average_monthly_change:,.2f}".replace('$-','-$'))
print(f"Greatest Increase in Profits: ${Greatest_Increase:,.0f}".replace('$-','-$'))
print(f"Greatest Decrease in Profits: ${Greatest_Decrease:,.0f}".replace('$-','-$'))
    
    


    


       
   