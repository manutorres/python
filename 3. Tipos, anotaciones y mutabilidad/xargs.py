def multiplicar(*numbers):
    total = 1
    print(type(numbers))
    for number in numbers:
        total *= number
    return total


result = multiplicar(2, 3, 4)
print(result)
