low = 1
high = 1000

print("Por favor piense en un número entre {} y {}".format(low, high))
input("Presione ENTER para comenzar")

# Algoritmo de Binary Search (Búsqueda Binaria)
count = 0
while True:
    guess = low + (high - low) // 2
    count += 1
    high_low = input("Mi estimación es {}. Tendría que adivinar mayor o menor? "
                     "Ingrese + o -, o c si adiviné correctamente: "
                     .format(guess)).casefold()
    if high_low == "+":
        low = guess + 1
    elif high_low == "-":
        high = guess - 1
    elif high_low == "c":
        # print("Lo adiviné en {} intentos!".format(count))
        print(f"Lo adiviné en {count} intentos!")
        break
    else:
        print("Por favor ingrese +, -, o c")
