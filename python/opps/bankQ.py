class bankAccount:

    acc_num = 10101010 
    balance = 100 

class savingsAccount(bankAccount):
    interest_rate = 10

    def calculate(self, i):
        return self.interest_rate
    
class test:
    saving = savingsAccount()
    saving.calculate()


