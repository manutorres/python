name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name))) # Cast a int para evitar errores
print(age)

# Comentario multilinea con Ctrl + /
# if age >= 18:
#     print("You are old enough to vote")
#     print("Please put an X in the box")
# else:
#     print("Please come back in {0} years".format(18-age))

# Mismo resultado con la condicion invertida
if age < 18:
    print("Please come back in {0} years".format(18-age))
elif age == 900:
    print("Sorry, Joda, you die in return of the Jedi")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")

# Comentario para notar el git diff