import time

# print(time.time())


def enviar_emails():
    for i in range(10000):
        pass


principio = time.time()
print(principio)
enviar_emails()
fin = time.time()
print(fin)
duracion = fin - principio
print(duracion)
