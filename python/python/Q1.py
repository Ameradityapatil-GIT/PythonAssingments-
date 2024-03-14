#WAP Take input of age of 3 people by user and determine oldest and youngest among them.
#Q1
# person1 = input("Enter the age of first person")
# person2 = input("Enter the age of second person")
# person3 = input("Enter the age of third person")

# if person1>person2>person3:
#     print("The Fist person is oldest")
# elif person2>person1>person3:
#     print("the second is oldest")
# else:
#     print("The third person is oldest")   

#loop pratice 
# Q1
# num = 0
# sum = 0
# while(num<100):
#     num = num+1
#     sum = num+sum
#     print(num)



#print(sum)    

# Q2     
#Write a program to print all prime number in between 1 to 100.

for i in range(1,6):
    for j in range(1,i+1):
     print("* " , end="")
    print()
        


for num in range(100, 1000):
    temp = num
    sum = 0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num)


