num1 = 0 #even
num2 = 0 #odd
evenrange = int(input("Enter range of even want to see"))
oddrange = int(input("Enter range of odd want to see"))
for num1 in range(0,evenrange,2):
    print(num1)

for num2 in range(0,oddrange,3):
    print(num2)
