#leap year concept = most years hat can be divided by 4 are leap years
#but if year is century year, it should be divisible by 400 to be a leap year
#e.g. 1900 is not a leap year because it's century year but not divisible by 400

import random
year = random.randint(1990,2024)
print(year)
if year%4==0 and year%100!=0 or year%400==0:
    print(f"Given {year} is a leap year")
else:
    print(f"Given {year} is not a leap year")