# This file demonstrates my first experience of Python as a programming language.
# We learnt about variables and inputs and printing variables. 


firstname = input("Please enter your first name")
lastname = input("Please enter your surname")
print ("Hello" + firstname + lastname)



number1 = float(input("Please enter the first number:"))
number2 = float(input("Please enter the second number:"))
answer = number1 + number2

print(number1, "+", number2, "=", answer)

textvar1 = "I Like 4 Pies"
numvar1 = 34

textvar2 = textvar1.isalnum()
numvar2 = numvar1.bit_count()

print (textvar2)
print (numvar2)

number1 = input("Enter whole number: ")
number2 = input("Enter decimal number: ")

integer_number = int(number1)
float_number = float(number2)
round_number = int(round(float_number))

print(number1)
print(number2)
print(round_number)

#Pet
name = "Pep Guardogiola"
age = 2
bark = True
tweet = False

print("My pet is called", name, ", He is", age, "years old")
print("Statement:", name, "barks.", bark)
print("Statement:", name, "tweets.", tweet)