import json
from pathlib import Path

peliculas = [
    {"id": 1, "titulo": "Terminator", "fecha": 1984},
    {"id": 2, "titulo": "Robocop", "fecha": 1990}
]

data = json.dumps(peliculas)
# print(data)
path = Path("peliculas.json")
path.write_text(data)

data = path.read_text()
peliculas = json.loads(data)
print(peliculas[0]["titulo"])
