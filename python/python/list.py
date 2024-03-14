# list = []

# print(list)

# length = list.__len__()

# for i in range(length-1,-1,-1):
#     if(list[i]%2!=0):
#         print(list[i],end= " ")

# finding greatest and samallest

 
# for i in range(list ):




# smaller = list[0]
# larger = list[0]

# for i in range(1, len(list)):
#     if list[i] < smaller:
#         smaller = list[i]
#     elif list[i] > larger:
#         larger = list[i]

# print("Smallest element is:", smaller)
# print("Largest element is:", larger)


#searching 
# list = [3,7,8,10,20,24]

# catch = int(input("enter the value")) 
# x = len(list)
# for i in range(0,x):
#     if(list[i]==catch):
#         print(cautch)
#     else:
#         print("-1")    

# Q Generate a list of squares for numbers 1 to 10 using list comprehension. Print the resulting list.


# list = [1,2,3,4,5,6,7,8,9,10]


# square_list = [x*2 for x in range(11)]

# print(square_list)

# Q Take a list of words and sort them in alphabetical order. Print the sorted list.

# list = ['a','c','e','f','g','b']


# sorted(list)
# print(sorted(list))
# for i in range(len(list)):
#         for j in range(i):
#             list[j] = list[j+1]

#  Given a list of ages, filter out the adults (age >= 18). Print the modified list.

list = [28,19,18,30,15,25,90,17,14]
ad_list = []

# for i in range(0,len(list)):
#     if list[i] >= 18:
#         ad_list.append(list[i])
        
# print(ad_list)


# for i in list:
#     if i >=18:
#         ad_list.append(i)


# print(ad_list)



# Create two lists of colors and concatenate them. Print the combined list

# color = ['red','green','black','white']
# secondcolor = ['silver','gold','brown']


# all = color + secondcolor
# print(all)
# color.append(secondcolor)

# print(color)

# Given a list of animals, remove a specific animal from the list. Print the modified list.

list = {'a','b,','c','d'}

list.remove("a")
# list.pop(0)

print(list)


