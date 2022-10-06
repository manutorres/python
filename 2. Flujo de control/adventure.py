available_exits = ["norte", "sur", "este", "oeste"]
chosen_exit = ""
while chosen_exit not in available_exits:
    chosen_exit = input("Por favor elija una dirección: ")
    if chosen_exit.casefold() == "salir":
        print("Game over")
        break

print("Lograste salir!")
