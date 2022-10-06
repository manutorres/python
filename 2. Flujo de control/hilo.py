low = 1
high = 1000

print("Please think of a number between {} and {}".format(low, high))
input("Press ENTER to start")

count = 0
while True:
    guess = low + (high - low) // 2
    count+1
    high_low = input("My guess is {}. Should I guess higher or lower? "
                    "Enter h or l, or c if my guess was correct: "
                     .format(guess)).casefold()
    if high_low == "h":
        low = guess + 1
    elif high_low == "l":
        high = guess - 1
    elif high_low == "c":
        # print("I got in {} guesses!".format(count))
        print(f"I got in {count} guesses!")
        break
    else:
        print("Please enter h, l or c")
