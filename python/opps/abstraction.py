from abc import ABC, abstactmethod  #<--decorator 

#this is an multi level inheritance eg
#we can't make objects of any abstract class 
class car:
    @abstactmethod #anotation
    def engin(self):
        pass
    @abstactmethod    
    def chasis(self):1
    pass
    @abstactmethod
    def control(self):
        pass
    @abstactmethod
    def fuel(self):
        pass

    def wheels(self):
        return 4

class honda(car):
    def engin(self):
        return "V8 engin"
    def chasis(self):
        return "sedan"
    
    def control(self):
        return "automatic"
    def fuel(self):
        return "Hybrid"    
    

class maruti(car):
    
    def engin(self):
        return "V1 engin"
    def chasis(self):
        return "sedan"
    
    def control(self):
        return "Manauel"
    def fuel(self):
        return "petrol"


