
# 0, 0.0, 0j == False
if 0:
    print("Verdadero")
else:
    print("Falso")

# "" == False
name = input("Por favor, ingrese su nombre:")
if name != "":
    print("Hola, {}".format(name))
else:
    print("Sos la persona sin nombre?")
