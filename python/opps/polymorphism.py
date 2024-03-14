# class A:
#     def run(self):
#         print("A is running")

# class B(A):
#     def run(self):
#         print("B is running")

# class C(A):
#     def run(self):
#         print("C is running")

# class test:
#     b = B()
#     c = C()
#     b.run()
#     c.run()

#1 Define a base class `Shape` with a method `area` that returns 0. Create a derived class `Circle` that inherits from `Shape` and overrides the `area` method to calculate the area of a circle. Provide sample input and expected output.

# class shape:
    
#     def area(self):
#         return 0     
        

# class circle(shape):
#     redius = 5
#     def area(self):
#         return 3.14 * (self.redius * self.redius)



# class triangle(shape):
#     height = 10
#     breadth = 5
#     def area(self):
#         return 1/2 * self.breadth * self.height    
    

# class test:
#     c = circle()
#     # print(c.area())
#     t = triangle()
#     print(t.area())


# Create a base class `Vehicle` with a method `fuel_efficiency` that returns 0. Derive a class `Car` from `Vehicle` and override the `fuel_efficiency` method to calculate the efficiency of a car. Provide sample input and expected output.
# class Vehicle:
#     def fuel_efficiency(self):
#         return 0
# class car(Vehicle):
#     distance = 300
#     fuel_consumed= 20
#     def fuel_efficiency(self):
#         return self.distance / self.fuel_consumed
# class test:
#     c = car()
#     print(c.fuel_efficiency())

# Design a class hierarchy with a base class `Animal` and derived classes `Dog` and `Cat`. Override a method `sound` in each derived class to return the sound each animal makes. Provide sample input and expected output.
# class animal:
#     def sound(self):
#         print("makes a sound")

# class dog(animal):
#     def sound(self):
#         print("Dog barks ")

# class cat(animal):
#     def sound(self):
#         print("cat meows")
# class test:
#     d = dog()
#     d.sound()
#     c = cat()
#     c.sound()        
# Implement a base class `Person` with a method `greet` that returns "Hello!". Create a derived class `Student` from `Person` and override the `greet` method to return "Hi there!". Provide sample input and expected output    

# class person:
#     def greet(self):
#         print("Hello!")
# class student(person):
#      def greet(self):
#         print("Hello there!!")

# class test:
#     s = student()
#     s.greet()

# Create a base class `Employee` with a method `calculate_salary` that returns 0. Derive a class `Manager` from `Employee` and override the `calculate_salary` method to include a bonus. Provide sample input and expected output.
class Employee:
    def calculate_salary(self):
        return 0
class Manager(Employee):
        salary = 5000
        bonus = 1000
        def calculate_salary(self):
            return self.salary + self.bonus

class test:
     m = Manager()
     print(m.calculate_salary())