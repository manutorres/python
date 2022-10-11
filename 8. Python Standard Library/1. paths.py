from pathlib import Path

Path(r"C:\Program Files")  # Raw string: no escapea caracteres
Path("usr/local/bin")

Path() / "directorio" / "otro-directorio"
Path.home()

path = Path(__file__)  # Evita que tome config del IDE como direccion
print(path.exists())
path.is_file()
path.is_dir()

print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
print(path.absolute())
path.with_name("otro.py")  # Misma ruta, distinto nombre y extencion
path.with_suffix(".txt")  # Misma ruta, mismo nombre, distinta extencion
