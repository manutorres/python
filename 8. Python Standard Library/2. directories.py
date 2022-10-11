from pathlib import Path

path = Path(__file__).parent

for p in path.iterdir():
    print(p)

paths = [p for p in path.iterdir() if p.is_file()]
print(paths)  # Lista de PosixPaths o WindowsPaths

# Para generar recursivamente buscando por patron
archivos_py = [p for p in path.glob("**/*.py")]
archivos_py = [p for p in path.rglob("*.py")]
print(archivos_py)  # Lista de PosixPaths o WindowsPaths
