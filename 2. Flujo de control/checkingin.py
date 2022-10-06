parrot = "Azul Turqueza"

letter = input("Ingrese un caracter: ")

if letter in parrot:
    print("{} está en {}".format(letter, parrot))
else:
    print("No tengo esa letra")

print("-" * 80)

activity = input("Qué te gustaría hacer hoy? ")

if "cine" not in activity.casefold():  # lowercase con mejor trato de algunos caracteres
    print("Pero yo quiero ir al cine")
