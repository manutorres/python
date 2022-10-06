shopping_list = ["leche", "pasta", "huevos", "queso", "pan", "arroz"]

item_to_find = "pollo"
found_at = None

# for index in range(6)
# for index in range(len(shopping_list)):
#     if shopping_list[index] == item_to_find:
#         found_at = index
#         break

if item_to_find in shopping_list:
    found_at = shopping_list.index(item_to_find)

if found_at != None:
    print("Item encontrado en la posición {}".format(found_at))
else:
    print("{} no encontrado".format(item_to_find))
