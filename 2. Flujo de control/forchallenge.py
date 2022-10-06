# For loop with step
# Write a program to print out all the numbers from 0 to 100 that are divisible by 7.
# Note that zero is considered to be divisible by all other integers, so your output should include zero.

divisible_by_7 = []
for div in range(0, 101, 7):
    divisible_by_7 += [div] # Union de listas

print(divisible_by_7)

