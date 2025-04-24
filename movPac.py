import random

def generar_movimientos(n=100):
    movimientos = []
    direccion_anterior = random.randint(1, 4)
    movimientos.append(direccion_anterior)

    opuestos = {1: 2, 2: 1, 3: 4, 4: 3}

    for _ in range(n - 1):
        posibles = [direccion_anterior] * 5
        for dir in range(1, 5):
            if dir != direccion_anterior and dir != opuestos[direccion_anterior]:
                posibles.append(dir)
        nueva_direccion = random.choice(posibles)
        movimientos.append(nueva_direccion)
        direccion_anterior = nueva_direccion

    return movimientos

# Generar y mostrar los movimientos en formato MARIE
movs = generar_movimientos()
for mov in movs:
    print(f"DEC {mov}")