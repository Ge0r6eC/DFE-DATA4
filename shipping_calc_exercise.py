# An online retailer provides express shipping for many of its items at a rate of $10.95
# for the first item, and $2.95 for each subsequent item. Write a function that takes the
# number of items in the order as its only parameter. Return the shipping charge for
# the order as the function’s result. Include a main program that reads the number of
# items purchased from the user and displays the shipping charge.


def cost_shipping(num_items):
    cost = float(round(((num_items - (num_items -1))*10.95) + ((num_items-1)*2.95), 2))
    print(cost)
    return cost

purchased_items = int(input("How many items have you purchased?? "))


print(f"As you have purchased {purchased_items} item/s, then the express shipping cost will be £{cost_shipping(purchased_items)}. Thank you")



#n - (n-1) = 1  5 - 4 = 1   73 - 72 = 1



