
with open("teams.txt", "w") as myfile:
    teams = ["Clippers", "\n", "Timberwolves", "\n", "Pelicans", "\n", "Jazz", "\n", "Lakers","\n"]
    myfile.writelines(teams)


myfile = open ("teams.txt", "r")

teams2 = myfile.readlines()

print(teams2[0])
print(teams2[3])

myfile.close()

with open("teams.txt", "w") as myfile:
    new_first_line = "This is a list of teams" + '\n'
    teams2.insert(0, new_first_line)
    myfile.writelines(teams2)

