name = input("Por favor ingrese su nombre: ")
age = int(input("Cuántos años tenés, {}? ".format(name)))

if 18 <= age < 31:
    print("Bienvenido a las vacaciones de 18 a 30, {0}!".format(name))
else:
    print("Lo siento, no tiene permitido el ingreso")
