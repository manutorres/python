print("Today")
print('fun')
print('We can include "quotes" in strings')
print("hello" + "world")

greeting = "Hello"
name = 'Manu'

print(greeting + ' ' + name)

age = 24
print(age)

print(type(greeting))
print(type(age))

age_in_words = "2 years"
# print(name + " is " + age + " years old")   # Error por concatenacion de str e int
print(type(age))

print(name + f" is {age} years old")

print(f"Pi is approximately {22/7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")