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

# initiating the writing to text file process.

# opening up datafile as object.
with open("budget_data.csv", newline='') as myFile:
       
    # setting datafile as csv reader object.
    reader = csv.reader(myFile, delimiter=',')

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
            Greatest_Increase_Index = monthlychanges.index(Greatest_Increase)       
        
        # Calculate Greastest Monthly Decrease in Earnings
        elif int(difference) < Greatest_Decrease:
            Greatest_Decrease = int(difference)
            Greatest_Decrease_Index = monthlychanges.index(Greatest_Decrease)
        
        # calculate average monthly change
        average_monthly_change = int(difference_total)/int(monthdiffcount)
    
# Going to Match Up the Index of Greastest Increase and Decrease in Earnings Month with its respected months in the original data file.
with open("budget_data.csv", newline='') as myFile:
    reader = csv.reader(myFile, delimiter=',')
    
    next(reader)
    
    # have to account that there is one less data entry in monthlychange list, because we exclude the first month.
    monthcount1 = -1

    for row in reader:
        if monthcount1 == int(Greatest_Increase_Index): 
            Greatest_Increase_Month = row[0]   
       

        elif monthcount1 == int(Greatest_Decrease_Index):
            Greatest_Decrease_Month = row[0]   
        
        monthcount1 += 1  


    # printing the results/analysis of our dataset
    print(f"Total Months: {monthcount}")
    print(f"Total: ${net_profit:,.0f}".replace('$-','-$'))
    print(f"Average Change: ${average_monthly_change:,.2f}".replace('$-','-$'))
    print(f"Greatest Increase in Profits: {Greatest_Increase_Month} (${Greatest_Increase:,.0f})".replace('$-','-$'))
    print(f"Greatest Decrease in Profits: {Greatest_Decrease_Month} (${Greatest_Decrease:,.0f})".replace('$-','-$'))



        


       
   