marks = int(input("Enter marks to assign grade : "))
if (marks >= 90 and marks<=100):
    print("Grade - A")
elif (marks >= 80 and marks < 90):
    print("Grade - B")
elif (marks >= 70 and marks < 80):
    print("Grade - C")
    print("Work Harder!! - Do your best on next")
elif(marks >= 60 and marks < 70):
    print("Grade - D")
    print("Ver close to failing - Need to do hard work")
elif (marks<60):
    print("Fail")
else:
    print("Entering invalid marks")
print("Bye")