year = 1900
month = 1
day = 1 #withinmonth
dayinweek = 0 #totaldays, badly named variably -- sorry
leap = False 
month_30 = [9, 4, 6, 11]
suncount = 0

while year <= 2000:
    dayinweek += 1

    if dayinweek % 7==0 and year > 1900 and day==1:
        suncount += 1

    if year % 4 == 0: leap = True
    else: leap = False

    if leap == True and month == 2 and day >= 29:
        month += 1
        day = 1
        continue 
    if leap == False and month == 2 and day >= 29: 
        month += 1
        day = 1
        continue 

    if month in month_30 and day >= 30:
        day = 1
        month += 1
        continue

    if month not in month_30 and day >= 31 and month != 12:
        month += 1
        day =1
        continue

    if month == 12 and day >= 31:
        day = 1
        month = 1
        year += 1
        continue 

    day += 1
    
print(suncount)

    

    




    
    


