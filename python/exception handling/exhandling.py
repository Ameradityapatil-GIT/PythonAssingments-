x = int(input())
y = int(input())

try: 
    print(x/y)

except:
    ZeroDivisionError
    print("You can not divide it by zero")