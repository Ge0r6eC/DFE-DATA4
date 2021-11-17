# import pdb
# pdb.set_trace()


# # a = "aaa"
# # b = "bbb"
# # c = "ccc"

# # def final(var1, var2, var3):

# #     return(var1+var2+var3)

# # print(final(a,b,c))



# # user_funds = 10.31
# # item_price = float(input("Burger price: "))

# # if item_price < user_funds:
# #     print("You have enough money!")
# # if item_price == user_funds:
# #     print ("You have the precise amount of money"

# # if item_price > user_funds:
# #     print ("Sorry you don't have enough money")

# # def product(n):
# #     total = 1
# #     for i in n:
# #         total *= i
# #     return total

# # print(product([4,4,5]))

# def is_prime(x):
#     if x < 2:
#         return False
#     else:
#         for n in range(2, x-1):
#             if x % n == 0:
#                 return False
#     return True

# x = int(input("Enter a number and I will tell you if it is a prime"))

# if is_prime(x):
#     print(f"{x} is a prime number")
# else:
#     print(f"{x} is not a prime number") 


item_list = ["Burger", "Hotdog", "Bun", "Ketchup", "Cheese"]
n = 0

while n < 5:
    for i in item_list:
        print(i)
    n += 1
print(item_list[4])


