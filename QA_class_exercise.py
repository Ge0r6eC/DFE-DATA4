
class Student:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def grade_score(self, score1, score2, score3):
        av_score = (score1 + score2 + score3)/3
        return(int(av_score))



John = Student("John", "21")
Jane = Student("Jane", "22")
James = Student("James", "19")
Jim = Student("Jim", "20")
Jake = Student("Jake", "20")

print(Jake.grade_score(30,20,10))

print(Jane.grade_score(30,12,28))

print(James.grade_score(30,20,10))

print(f"{James.name} is called {James.name} and he is {James.age} years old. His average score across 3 tests is {James.grade_score(30,20,10)} ")
print(f"{John.name}'s full name is actually Jonathan, but he prefers {John.name}")
print(f"{Jim.name} at {Jim.age} is older than {James.name} but younger than {Jane.name}")
print(f"{Jake.name} is only {Jake.age} but is way smarter than the older {Jane.name}, {Jane.age}, as you can see with his test score of {Jake.grade_score(30,25,30)} compared to {Jane.name}'s lowly {Jane.grade_score(10,10,10)}")

