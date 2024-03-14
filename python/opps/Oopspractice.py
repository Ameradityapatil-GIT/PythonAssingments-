# Create a class called Product with attributes for name, price, and quantity. Create a constructor for the class that initializes these attributes
class product:
    name = None
    price = 10
    quant = 10
    def __init__(self,p,q,n):
        self.name = n
        self.price = p  
        self.quant = q

#  Create a class called Customer with attributes for name and address. Create a constructor for the class that initializes these attributes.    

class customer:
    name = None
    address = None
    def __init__(self,n,a) :
        self.name = n 
        self.address = a


def calculate_total(self,p,q):
    return q*p.price
        

class test:
    pen = product("pen",20,1)
    calculate_total(pen,10)     




#  Create a function called calculate_total that takes a Product object and a quantity as arguments and returns the total price for that quantity of the product.

     