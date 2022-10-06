def multiply(*numbers):
    total = 1
    print(type(numbers))
    for number in numbers:
        total *= number
    return total


result = multiply(2, 3, 4)
print(result)
