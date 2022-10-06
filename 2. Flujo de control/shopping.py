shopping_list = ["leche", "pasta", "huevos", "queso", "pan", "arroz"]

for item in shopping_list:
    if item == "queso":
        continue
    print("Comprar " + item)

for item in shopping_list:
    if item == "queso":
        break
    print("Comprar " + item)
