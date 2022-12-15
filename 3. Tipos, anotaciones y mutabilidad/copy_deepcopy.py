from copy import copy, deepcopy

# COPY

l1 = [1, 2, {"valor": 3}]

l2 = copy(l1)
print("L1:", l1)
print("L2:", l2)

l2[1] = 5
l2[2]["valor"] = "A"
print("L1:", l1)
print("L2:", l2)

print()
# DEEPCOPY

l1 = [1, 2, {"valor": 3}]
l2 = [4, 5, {"valor": 6}]

l2 = deepcopy(l1)
print("L1:", l1)
print("L2:", l2)

l2[1] = 5
l2[2]["valor"] = "A"
print("L1:", l1)
print("L2:", l2)
