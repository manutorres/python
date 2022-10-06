age = 24
print("Mi edad es " + str(age) + " años")   # Forma tradicional de coercion
print("Mi edad es {0} años".format(age))    # Con reemplazo de campos

print("Hay {0} días en {1}, {2}, {3}, {4}, {5}, {6} y {7}"
      .format(31, "Ene", "Mar", "May", "Jul", "Ago", "Oct", "Dic"))

print("Ene: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Ago: {1}, Sep: {2}, Oct: {2}, Nov: {1}, Dic: {2})"
      .format(28, 30, 31))

print("""
Ene: {2}, 
Feb: {0}, 
Mar: {2}, 
Apr: {1}, 
May: {2}, 
Jun: {1}, 
Jul: {2}, 
Ago: {1}, 
Sep: {2}, 
Oct: {2}, 
Nov: {1}, 
Dic: {2}
""".format(28, 30, 31))
