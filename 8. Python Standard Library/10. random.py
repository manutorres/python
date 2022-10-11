import random
import string

print(random.random())
print(random.randint(1, 10))
print(random.choice([1, 2, 3, 4]))
print(random.choices([1, 2, 3, 4], k=2))

# Random password
print("".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=8)))
print("".join(random.choices(string.ascii_letters + string.digits, k=8)))

numeros = [1, 2, 3, 4]
random.shuffle(numeros)
print(numeros)
