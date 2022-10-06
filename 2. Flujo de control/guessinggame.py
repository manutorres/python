import random

highest = 10
answer = random.randint(1, highest)
print(answer)   # TODO: Remove after testing

# Version 1
# print("Please guess number between 1 and {}: ".format(highest))
# guess = int(input())
# while True:
#     if guess == answer:
#         print("You guessed it right!")
#         break
#     elif guess == 0:
#         print("You chose to quit the game")
#         break
#     else:
#         if guess < answer:
#             print("Please guess higher")
#         else:
#             print("Please guess lower")
#         guess = int(input())

# Version 2
print("Please guess number between 1 and {}: ".format(highest))
guess = int(input())
while guess != answer and guess != 0:
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess = int(input())

if guess == answer:
    print("You guessed it right!")
else: # guess == 0
    print("You chose to quit the game")


# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")


# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time")

