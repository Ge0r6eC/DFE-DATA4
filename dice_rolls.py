import ran_num_gen

dice_roll1 = ran_num_gen.dice()

dice_roll2 = ran_num_gen.dice()


print("roll the dice twice and see what you get...")

shall_roll = input("tell me to roll if you dare... ").lower()

if shall_roll == ("roll"):
    print(f"you rolled {dice_roll1} and a {dice_roll2}")
else:
    print("That is not the magic word, guess again...")
