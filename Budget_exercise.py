#Goal: “Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. 
#These objects should allow for depositing and withdrawing funds from each category, as well computing category balances and transferring 
#balance amounts between categories”

class Budget:
    
    balance = 0

    def deposit(self, moneyin):
        self.balance += moneyin
        return self.balance

    def withdraw(self,moneyout):
        self.balance -= moneyout
        return self.balance 
    
    def transfer(self,moneyacross,budgetName):
        self.balance -= moneyacross
        budgetName.deposit(moneyacross)



food = Budget()
clothes = Budget()
entertainment = Budget()

food.deposit(15)
food.withdraw(1)
food.transfer(10, clothes)

clothes.deposit(10)
clothes.withdraw(7)

entertainment.deposit(30)
entertainment.withdraw(20)
entertainment.transfer(10, food)

print(food.balance)
print(clothes.balance)
print(entertainment.balance)


