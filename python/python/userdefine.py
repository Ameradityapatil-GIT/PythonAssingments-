# def prime():
#     num = int(input("Enter a number: "))  
  
#     if num > 1:  
#         for i in range(2,num):  
#          if (num % i) == 0:  
#             print(num,"is not a prime number")  
#             print(i,"times",num//i,"is",num)  
#             break  
#         else:  
#             print(num,"is a prime number")  
    
#     else:  
#         print(num,"is not a prime number")  



# def armstrong():
#     num = int(input("Enter a number: "))  
#     sum = 0  
#     temp = num  
  
#     while temp > 0:  
#         digit = temp % 10  
#         sum += digit ** 3  
#         temp //= 10  
  
#     if num == sum:  
#         print(num,"is an Armstrong number")  
#     else:  
#         print(num,"is not an Armstrong number")



# armstrong()