parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")

print("-" * 80)

activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold(): #lowercase con mejor trato de algunos caracteres
    print("But I want to go to the cinema")