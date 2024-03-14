#single inheritance
# class demo :
#     x = 4 
#     def run(slef):
#         print("demo running")


# class test(demo):
#     y = 3
#     def show(slef):
#         print("Test showing")


# class xyz :
#     t = test()
#     t.show()
#     print(t.y)
#     print(t.x)


#hierichical inheritance 
# class human:
#     def talk(self):
#         x =10
#         print("can talk")
#     def walk(self):
#         print("is walking")

# class student(human):
#     def student(self):
#         print("is studing")

# class employe(human):
#     def work(self):
#         print("working")
# class test():
    
#     c = student()
#     c.talk()
#     d = employe()
#     d.walk()
    # print()
# multilevel inheritance
# class grandfather:
#     def show(self):
#         print("is show")

# class father(grandfather):
#     def display(self):
#         print("is display")
# class son(father):
#     def run():
#         print("is running")
# class test:
#     c = son()
#     c.display()
#     c.show()                    

#multiple inheritance 

class A :
    def run(self):
        print("A is running")
class B:
    def run(self):
        print("B is running")
class c(A,B):
    def display(self):
        print("is displaying")                 

class test:
    c = c()
    c.run()      #ambiguity
    c.run()
    # c.display()