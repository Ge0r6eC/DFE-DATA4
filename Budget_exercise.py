#Goal: “Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. 
#These objects should allow for depositing and withdrawing funds from each category, as well computing category balances and transferring 
#balance amounts between categories”

class Budget:
    
    def __init__(self, name):
        self.balance = 0
        self.name = name

    def deposit(self, moneyin):
        self.balance += moneyin
        return self.balance

    def withdraw(self,moneyout):
        if self.balance >= moneyout:
            self.balance -= moneyout
            return self.balance 
        else:
            print(f"Sorry, you do not have the funds in {self.name} to withdraw this amount")
            return self.balance
    
    def transfer(self,moneyacross,budgetName):
        if self.balance >= moneyacross:
            self.balance -= moneyacross
            return budgetName.deposit(moneyacross)
        else:
            print(f"Sorry, you do not have the funds in {self.name} to transfer this amount")
            return self.balance



food = Budget("Food Budget")
clothes = Budget("Clothes Budget")
entertainment = Budget("Entertainment Budget")

food.deposit(15)
food.withdraw(20)
food.transfer(10, clothes)
print(f"Your {food.name} balance is £{food.balance}")

clothes.deposit(10)
clothes.withdraw(7)
print(f"Your {clothes.name} balance is £{clothes.balance}")

entertainment.deposit(30)
entertainment.withdraw(20)
entertainment.transfer(5, food)
print(f"Your {entertainment.name} balance is £{entertainment.balance}")



