from pathlib import Path
from time import ctime
import shutil

path = Path(__file__)

path.exists()
# path.rename()
# path.unlink()
print(ctime(path.stat().st_ctime))

# Read se encarga de abrir y cerrar el archivo automaticamente
path.read_bytes()   # Contenido en binario
print(path.read_text())  # Contenido en string
# path.write_bytes()
# path.write_text("...")

# Copiar archivos no por contenido, sino usando utilidad de la shell
fuente = Path("fuente.txt")
destino = Path("destino.txt")
shutil.copy(fuente, destino)
