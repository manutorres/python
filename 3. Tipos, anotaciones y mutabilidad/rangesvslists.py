# Ambos son iterables

# La lista almacena los 5 valores en memoria
l = [1, 2, 3]
print(type(l))
for item in l:
    print(item)

print()

# El range es liviano porque permite iterar pero no almacena
r = range(1, 4)
print(type(r))
for item in r:
    print(item)
