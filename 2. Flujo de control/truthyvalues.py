
# 0, 0.0, 0j == False
if 0:
    print("True")
else:
    print("False")

# "" == False
name = input("Please enter your name:")
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")