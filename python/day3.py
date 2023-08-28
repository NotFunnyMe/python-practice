for i in range(10):
    print("count",i+5)
    if i+5>=11:
        break

for i in range(10):
    if i<5:
        continue
    print(i)

ch=0
while True:
    ch=input("do u wish to continue y/n")
    if ch=='y':
        print("continuing")
    if ch=='n':
        print("exiting")
        break