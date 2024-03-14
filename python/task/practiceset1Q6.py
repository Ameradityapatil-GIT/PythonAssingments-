# neg = int(input("enter the negative number"))
# pos = int(input("enter the posetive number"))
sum = 0
count=0
for i in range(1,10):
    neg = int(input("enter the negative number"))
    # pos = int(input("enter the posetive number")) 
    if(neg<0):
        count = count + 1
        print(i)