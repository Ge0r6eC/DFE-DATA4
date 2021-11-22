# This file demonstrates my learning about Lists and dictionaries
# We covered the difference between List, Dictionary and Tuple. 
# Mainly discussed how to print certain parts from the list. 

cool_cows = ["Winnie the Moo","Moolan", "Milkshake", "Mooana"]
cool_sheep = ["Baaaart", "Baaaaarnaby"]
cool_pigs = ["Chris P. Bacon", "Hamlet", "Hogwarts"]

cool_animals = [cool_cows, cool_sheep, cool_pigs]

print (cool_animals[1][0])

print ("Winnie the Moo" in cool_cows)
print ("Hamburger" in cool_pigs)


books = {"Killing Floor":"Lee Child", "The Bone Collector":"Jeffery Deaver",
"HP and the Philospher Stone":"J.K.Rowling", "Five go over the Hill":"Enid Blyton"}

#print(books["The Bone Collector"])
#print(books.keys())
books["The Hobbit"] = "JRR Tolkein"
print(books)
books["Fantastic Mr Fox"] = "Roald Dahl"
print (books)
