print("Hoy")
print('Hablamos de Python!')
print('Podemos incluir "comillas" en strings')
print("hello" + "world")

greeting = "Hola"
name = 'Python'

print(greeting + ' ' + name)

age = 24
print(age)

print(type(greeting))
print(type(age))

age_in_words = "2 años"
# print(name + " tiene " + age + " años")   # Error por concatenacion de str e int
print(type(age))

print(name + f" tiene {age} años")

print(f"Pi es aproximadamente {22/7:12.50f}")
pi = 22 / 7
print(f"Pi es aproximadamente {pi:12.50f}")
