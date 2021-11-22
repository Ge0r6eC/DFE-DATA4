# This demonstrates my learninig of IF / ELSE conditionals and also my learning of Loops - FOR and WHILE. 


devs_money = 100
dev_can_play_smash = True

if devs_money >10 and dev_can_play_smash:
    print("Dev enters a smash tourny!")
elif devs_money < 10 and dev_can_play_smash:
    print ("Dev is too poor to enter")
else:
    print("Dev just cant play smash")

Exam_Grade = int(input("Please type in your score "))
if Exam_Grade > 85:
    print ("Distinction, Well Done!")
elif Exam_Grade >= 65 and Exam_Grade <= 85:
    print ("Well Done, you have passed")
else:
    print ("You are not good enough. Har Har")


print("Pick a number, any number...")
num1 = int(input())

if num1 %2==0:
    print("This number is even")
else:
    print("This number is odd")


Name that shape exercise

print("Tell me the number of sides your shape has, and I'll tell you the shape!")
NumSides = int(input())
if NumSides >= 3 and NumSides <= 6:
    if NumSides == 3:
        print("I know that you are thinking of a Triangle")
    elif NumSides == 4:
        print("I know that you are thinking of a Square")
    elif NumSides == 5:
        print("I know that you are thinking of a Pentagon")
    else:
        print("I know that you are thinking of a Hexagon")
else:
    print("Please pick a number between 3 and 6, I am not a mind reader!")

tutorial on while loops
count = 0
name = str(input("What is your name?"))

while count < 5:
    print (name, "is awesome!")
    count += 1

for i in range(5, 11):
    print(i)

for i in range(10, 21, 2):
    print (i)

Write a while loop which asks for the names of 5 people, 
and for each person prints their name followed by the text "is awesome!"
count = 1
while count <= 5:
    name= str(input("What is your name?"))
    print(name, "is awesome")
    count += 1

Write a Python program to find those numbers which are 
divisible by 7 and multiple of 5, between 1500 and 2700 (both inc.)

for n in range(1500, 2701):
    if n%5 == 0 and n%7 == 0:
        print(n)

Write a Python program to convert temperatures to and from celsius,
fahrenheit.[ Formula : c/5 = f-32/9 [ where c = temperature
in celsius and f = temperature in fahrenheit ]

print("Use me to convert between Celsius and Farenheit")
print("Do you want to convert from C(celsius) or F(Farenheit)")
Convert = str(input())

if Convert == ("C"):
    tempC = int(input("Enter the temperature in Celsius here: "))
    
    tempF_convert = int(tempC*9/5 +32)
    print(f"{tempC}C is equal to {tempF_convert} Farenheit")
else:
    tempF = int(input("Enter the temperature in Farenheit here: "))
    
    tempC_convert = int((tempF-32)*5/9)
    print(f"{tempF}F is equal to {tempC_convert} Celsius")


