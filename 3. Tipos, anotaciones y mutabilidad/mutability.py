def modify_list(list_to_modify):
    list_to_modify[0] = "Valor nuevo"
    print("Direccion de memoria de lst antes: {}".format(id(list_to_modify)))
    print("Direccion de memoria de lst[0] antes: {}".format(
        id(list_to_modify[0])))


x = 1
print("Direccion de memoria de x: {}".format(id(x)))

x = x + 1
print("Direccion de memoria de x: {}".format(id(x)))

original_list = ["Un valor", "Otro valor"]
print("Direccion de memoria de original_list antes: {}".format(id(original_list)))
print("Direccion de memoria de original_list[0] antes: {}".format(
    id(original_list[0])))

modify_list(original_list)

print("Direccion de memoria de original_list despues: {}".format(id(original_list)))
print("Direccion de memoria de original_list[0] despues: {}".format(
    id(original_list[0])))
