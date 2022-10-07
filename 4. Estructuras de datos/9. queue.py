from collections import deque

cola = deque([])
cola.append(1)
cola.append(2)
cola.append(3)
cola.append(4)

cola.popleft()
print(cola)

if not cola:
    print("Cola vacia")
