# def add_calc(number1, number2): 
#     answer = number1 + number2
#     return answer

# added_number = add_calc(5,5)
# print(added_number + 20)


# create program that works out a grade based on marks 
# program should take the students name, homework score (/25), 
# assessment score (/50) and final exam score(/100) as inputs and
# output their name and final ICT grade as a percentage.

# def grade_calc(hmwk_score, asmt_score, fnex_score):
#     final_grade = ((hmwk_score + asmt_score + fnex_score) /175)*100
#     return final_grade


# student_name = input("Please enter the Student's name")
# homework_score = int(input("What was the homework score? /25"))
# assessment_score = int(input("What was the assessment score? /50"))
# final_exam_score = int(input("What was the final exam score? /100"))

# graded_percent_score = int(grade_calc(homework_score, assessment_score, final_exam_score))

# print (f"{student_name} your ICT Score is {graded_percent_score}%")

# if graded_percent_score >= 80:
#     print ("This equates to an A, well done")
# elif graded_percent_score >= 70:
#     print ("This equates to a B, well done")
# elif graded_percent_score >= 60:
#     print ("This equates to a C, well done")
# elif graded_percent_score >= 50:
#     print ("This equates to a D, unfortunatley you have not passed")
# else:
#     print("Unfortunately this means you have not registered a grade and therfore failed the test")


# write a Python function to multiply all the numbers in a list

# def product_calc(numbers):
#     total = 1
#     for i in numbers:
#         total *= i 
#     return total

# print (product_calc((8, 2, 3, 7)))

# 60% sale. want a printed discount table that shows the original 
# prices and the prices after the discount has been applied. 
#Original prices - £4.95, £9.95, £14.95, £19.95, £24.95

original_price = [4.95, 9.95, 14.95, 19.95, 24.95]
print ("Price | Discount | Sale Price")
print ("---------------------------")
for price in original_price:
    sale_price = round(price * 0.4, 2)
    print (f"{price}  | 60%     | {sale_price}")

#write a program that reads prices from the user until a blank
#line is entered. Display the total cost of all the entered items 
#on one line, followed by the amount due if the customer pays with
#cash on a second line.
#the amount due should be rounded to the nearest 5. 
#one way to compute the cash payment amount is to begin by determinin
# how many pennies would be needed to pay the total. then compute
#the remainder when this is divided by 5. finally adjust the total 
#down if the remainder is less than 2.5. otherwise adjust total up.


items_price = int(input("Type in the price of the item: "))


