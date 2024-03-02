import datetime
s = datetime.date.today()   #gives today date and time
print(s)
q = datetime.date.today().strftime("%Y")    #converts the date into string format with year
r = datetime.date.today().strftime("%B")    #gives month
s = datetime.date.today().strftime("%d")    #gives day
print(q)
print(r)
print(s)
print("week no of month",datetime.date.today().strftime("%W"))  # gives week number in a month
print("weekday of the week",datetime.date.today().strftime("%w"))
print("day of the year",datetime.date.today().strftime("%j"))
print("day of the week",datetime.date.today().strftime("%A"))
print(datetime.datetime.now())