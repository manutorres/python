import sys
import impuestos
# from impuestos import * # Mala practica por posible sobreescritura
from impuestos import iva

# Lista de archivos donde Python busca los modulos importados
print(sys.path)

print(iva())
