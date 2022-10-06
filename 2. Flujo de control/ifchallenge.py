name = input("Please enter your name: ")
age = int(input("How old are you, {}? ".format(name)))

if 18 <= age < 31:
    print("Welcome to 18-30 holidays, {0}!".format(name))
else:
    print("Sorry, you aren't allowed here")