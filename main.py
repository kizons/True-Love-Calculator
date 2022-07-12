print("WELCOME TO TRUE LOVE CALCULATOR!")
name = input("What is name ? \n").lower()
partner = input("What is your partner's name ? \n").lower()
add_names = str(name) + str(partner)

true = str(add_names.count("t") + add_names.count("r") + add_names.count("u") + add_names.count("e"))
love = str(add_names.count("l") + add_names.count("o") + add_names.count("v") + add_names.count("e"))

love_score = int(true + love)

if love_score > 50:
    print(f"Your Love Score is: {love_score}%\nYou are compatible")
else:
    print(f"Your Love Score is: {love_score}%\nOMG! You are not compatible")
