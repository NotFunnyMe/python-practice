#1
print("hello world")

#2
a=int(input("enter the first number : "))
b=int(input("enter the second number : "))
sum=a+b
print(sum)

#3
a=int(input("enter the number : "))
sqrt=a**(1/2)
print(sqrt)

#4
a=int(input("enter the first number : "))
b=int(input("enter the second number : "))
temp=a
a=b
b=temp
print("number after swapping : a= ",a)
print("number after swapping : b= ",b)

#5
a=int(input("enter the number : "))
if (a%2==0):
     print("even number")
else:
     print("odd number")

#6
r=int(input("enter the radius of circle : "))
areacircle=3.14*(r**2)
print(areacircle)

#7
t=int(input("enter the digit in celcius u want to convert into farehniet : "))
tempf=(t*(9/5))+32
print(tempf)

#8
principle=float(input("enter the principle amount : "))
rate=float(input("enter the rate : "))
time=int(input("enter the time : "))
si=(principle*rate*time)/100
print(si)

#9
y=int(input("enter to year you want to know is it leap or not : "))
if (y%400==0)and(y%100==0):
    print("it is leap year")
elif (y%4==0)and(y%100!=0):
    print("it is leap year")
else:
    print("it is not a leap year")

#10
n = int(input("Enter the number to find factorial: "))
factorial = 1
if(n < 0):
    print ("Factorial cannot be calculated")
elif(n==0):
    print ("Factorial of the number is 1")
else:
    for i in range (1, n+1):
        factorial = factorial *i
    print ("Factorial of the given number is: ", factorial)

#11
a=int(input("enter the number you want find the multiplication table = "))
for i in range(0,11):
    print(a ,"*", i ,"=" ,a*i)

#12
terms = 10
n1=1
n2=2
count = 0
if terms<=0:
    print("please enter positive number")
elif terms ==1:
    print("fibonacci series of 1 is 1")
else:
    print("fibonacci series")
    while count<terms:
        print(n1)
        n3=n1+n2
        n1=n2
        n2=n3
        count +=1

#13
