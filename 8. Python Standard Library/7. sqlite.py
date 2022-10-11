import sqlite3
import json
from pathlib import Path

path = Path("peliculas.json")
peliculas = json.loads(path.read_text())
# print(peliculas)

# with sqlite3.connect("db.sqlite3") as connection:
#     command = "INSERT INTO Peliculas VALUES(?, ?, ?)"
#     for pelicula in peliculas:
#         connection.execute(command, tuple(pelicula.values()))
#     connection.commit()

with sqlite3.connect("db.sqlite3") as connection:
    command = "SELECT * FROM Peliculas"
    cursor = connection.execute(command)
    connection.commit()
    # for row in cursor:
    #     print(row)

    # El cursos se encuentra al final luego de iterar sobre cada fila
    peliculas = cursor.fetchall()
    print(peliculas)
