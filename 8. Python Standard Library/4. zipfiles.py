from pathlib import Path
from zipfile import ZipFile

path = Path(__file__).parent

with ZipFile("files.zip", "w") as zip:  # Cierra archivo automaticamente
    for p in path.rglob("*.*"):
        print(p.name)
        zip.write(p)

with ZipFile("files.zip", "r") as zip:
    print(zip.namelist())
    info = zip.getinfo("filename")
    print(info.file_size)
    print(info.compress_size)
    # zip.extractall("extraidos")
