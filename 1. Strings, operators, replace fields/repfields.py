age = 24
print("My age is " + str(age) + " years")   # Forma tradicional de coercion
print("My age is {0} years".format(age))    # Con reemplazo de campos

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
      .format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))

print("Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Aug: {1}, Sep: {2}, Oct: {2}, Nov: {1}, Dec: {2})"
      .format(28, 30, 31))

print("""
Jan: {2}, 
Feb: {0}, 
Mar: {2}, 
Apr: {1}, 
May: {2}, 
Jun: {1}, 
Jul: {2}, 
Aug: {1}, 
Sep: {2}, 
Oct: {2}, 
Nov: {1}, 
Dec: {2}
""".format(28, 30, 31))