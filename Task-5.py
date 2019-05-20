from datetime import date

year1 = int(input("Enter year of date 1 : "))
month1 = int(input("Enter month of date 1 : "))
day1 = int(input("Enter day of date 1 : "))

year2 = int(input("Enter year of date 2 : "))
month2 = int(input("Enter month of date 2 : "))
day2 = int(input("Enter day of date 2 : "))


date1= date(year1,month1,day1)
date2 = date(year2,month2,day2)

Day = date2 - date1

print(Day.days, "Days have been passed!")