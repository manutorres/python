from datetime import datetime, timedelta
import time

dt = datetime(2022, 1, 1)
dt = datetime.now()

# String a Objeto Datetime
dt1 = datetime.strptime("2022/01/01", "%Y/%m/%d")
dt2 = datetime.fromtimestamp(time.time())  # Ahora

# En formato Argentina
print(f"{dt1.day}/{dt1.month}/{dt1.year}")

# Objeto Datetime a string
print(dt2.strftime("%Y/%m"))

print(dt1 > dt2)

# Time delta = duracion
duracion = dt2 - dt1
print(duracion)
print("Dias", duracion.days)
print("Segundos", duracion.total_seconds())  # La duracion completa

dt3 = dt2 + timedelta(days=1)
print(dt3)
