
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]    # Reverso pero no incluye el primero
backwards = letters[25:-1:-1]   # De z a z sin incluirlo, o sea vacio
backwards = letters[25::-1]     # Reverso, incluye hasta el principio por no especificar
backwards = letters[::-1]       # Python idiom para el reverso de un string
print(backwards)

qpo = letters[-10:-13:-1]
print(qpo)
edcba = letters[4::-1]
print(edcba)
rev_last_8 = letters[:-9:-1]
print(rev_last_8)

# Python idioms
print(letters[-4:])     # Ultimos 4 caracteres de la secuencia
print(letters[-1:])     # Ultimo caracter
print(letters[:1])      # Primer caracter. Util porque no da error si el string es vacio