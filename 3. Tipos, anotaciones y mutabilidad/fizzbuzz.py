
# Implementacion con menos calculo pero variable extra
def fizz_buzz(input):
    result = ""
    if input % 3 == 0:
        result += "Fizz"
    if input % 5 == 0:
        result += "Buzz"
    if result == "":
        result = input
    return result


# Implementacion usando multiples sentencias return
def fizz_buzz_2(input):
    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz_2(15))
