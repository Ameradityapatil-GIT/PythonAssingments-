# Q1. Create a Python class Book with attributes title, author, and year_published.Include a method display_info() that prints these details
# class book:
#     title = 'cosmos'
#     aurthor = 'robin'
#     year_published = 1996

#     def display_info(self):
#        print("title:",self.title)
#        print("aurthor:",self.aurthor)
#        print("published in :",self.year_published)
    
# class test:
#     a = book()
#     a.display_info()

    
# 2. Write a program that reads lines from a text file named data.txt and counts thenumber of occurrences of the word "Python". Handle potential file errors (e.g.,FileNotFoundError)\

# print(file.readlines())
# for x in file:
#     print(x)
    
# try:
#     file = open("C:\\Users\\amera\\OneDrive\\Desktop\\python\\test\\file1.txt","r")
#     print(file.readlines())

# except FileNotFoundError:
#     print("file does not exist")


# file.close()


#33. Define a function divide(a, b) that calculates the division of two numbers. Use try...except to catch ZeroDivisionError and print a clear message if division by zero is attempted.


# def division():
#     a = int(input("enter the value of  a:"))
#     b = int(input("Enter the value of b:"))
        

# try:
#     print(a/b)

# except ZeroDivisionError:
#     print("problem accured")        