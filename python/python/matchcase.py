#Switch case/ Match case 
# num = int(input = print("Enter the value of day want to see"))

# match num:
#     case 1:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuesday")
#     case 4:
#         print("Wednesday")
#     case 5:
#         print("Thursday")
#     case 6:
#         print("Friday")
#     case 7:
#         print("Saturday")

#WAP to take a month from user and print its season
num1 = int(input("Enter the value to see season"))
match num1:
    case 1:
        print("Winter") #jan
    case 2:
        print("Winter") #feb
    case 3:
        print("summer") #mar
    case 4:
        print("Summer") #april
    case 5:
        print("Summer") #may
    case 6:
        print("Summer") #jun
    case 7:
        print("rainy") #july
    case 8:
        print("rainy") #aug
    case 9:
        print("rainy") #sep
    case 10:
        print("rainy") #oct
    case 11:
        print("winter") #nov
    case 12:
        print("winter") #dec   
    case _:
        print("invalid")

#WAP to Take input of age of 3 people by user and determine oldest and youngest among them.
