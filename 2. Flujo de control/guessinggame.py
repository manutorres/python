import random

highest = 10
answer = random.randint(1, highest)
print(answer)   # TODO: Borrar después de testear

# Version 1
# print("Por favor elija un número entre 1 y {}: ".format(highest))
# guess = int(input())
# while True:
#     if guess == answer:
#         print("Muy bien, lo adivinaste!")
#         break
#     elif guess == 0:
#         print("Eligió terminar el juego")
#         break
#     else:
#         if guess < answer:
#             print("Elija un número mayor")
#         else:
#             print("Elija un número menor")
#         guess = int(input())

# Version 2
print("Por favor elija un número entre 1 y {}: ".format(highest))
guess = int(input())
while guess != answer and guess != 0:
    if guess < answer:
        print("Elija un número mayor")
    else:
        print("Elija un número menor")
    guess = int(input())

if guess == answer:
    print("Muy bien, lo adivinaste!")
else:  # guess == 0
    print("Eligió terminar el juego")


# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Elija un número menor")
#     guess = int(input())
#     if guess == answer:
#         print("Muy bien, lo adivinaste!")
#     else:
#         print("Lo siento, no lo adivinaste correctamente")
# else:
#     print("Lo adivinaste en la primera!")


# if guess < answer:
#     print("Elija un número mayor")
#     guess = int(input())
#     if guess == answer:
#         print("Muy bien, lo adivinaste!")
#     else:
#         print("Lo siento, no lo adivinaste correctamente")
# elif guess > answer:
#     print("Elija un número menor")
#     guess = int(input())
#     if guess == answer:
#         print("Muy bien, lo adivinaste!")
#     else:
#         print("Lo siento, no lo adivinaste correctamente")
# else:
#     print("Lo adivinaste en la primera!")
