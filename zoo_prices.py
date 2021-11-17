#A particular zoo determines the price of admission based 
# on the age of the guest. 
# Guests 2 years of age and less 
# are admitted without charge. Children between 3 and 12 years
# of age cost $14.00. Seniors aged 65 years and over cost $18.00. 
# Admission for all other guests is $23.00. 
# - This looks like some sort of list?

# Create a program that begins by reading the ages of all of the guests in a group 
# from the user, with one age entered on each line. 
# - some sort of input
# - allow multiple entries in one pass

# The user will enter a blank line to indicate that there are
# no more guests in the group. 
# - This looks like a conditional 'if blank line then break'? 

# Then your program should display
# the admission cost for the group with an appropriate message. 
#  - We need to add up teh prices
# - We need to print some things
# - we need to print a messsage

# The cost should be displayed using two decimal places.
# - Can i find out how to format a float?

# age_of_guest = 1
# age_list=[]

# while age_of_guest != 0:
#     age_list.append(age_of_guest)
#     age_of_guest = int(input("Enter the age of the guest to pay the right price : "))


# no_of_guests = len(age_list)

# print(no_of_guests)

# print (age_list)

#store the prices of entry per category
baby_price = 0.00           
child_price = 14.00
adult_price = 23.00
senior_price = 18.00

#store the age limit of each category
baby_limit = 2
child_limit = 12
adult_limit = 64

#start a totaliser of total price
total = 0
 
#need to get an input from user
age_of_guests = (input("Enter the age of the guests in your party (blankspace to end) : "))

while age_of_guests != "":
    if int(age_of_guests) <= baby_limit:
        total = total + baby_price
    elif int(age_of_guests) <= child_limit:
        total = total + child_price
    elif int(age_of_guests) <= adult_limit:
        total = total + adult_price 
    else:
        total = total + senior_price
    age_of_guests = (input("Enter the age of the guests in your party (blankspace to end) : "))

print(f"The total price of entry will be £{8(total)} Thank you, enjoy your day.")


    



