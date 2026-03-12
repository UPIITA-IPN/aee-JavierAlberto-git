import sys

def euclides_extendido(a, b):
    intercambiado = False
    if a < b:
        a, b = b, a
        intercambiado = True

    x0, y0 = 1, 0
    x1, y1 = 0, 1

    while b != 0:
        q = a // b
        a, b = b, a % b
        nuevo_x = x0 - q * x1
        nuevo_y = y0 - q * y1
        x0, x1 = x1, nuevo_x
        y0, y1 = y1, nuevo_y

    if intercambiado:
        return a, y0, x0
    else:
        return a, x0, y0


def leer_entrada():
    # Caso 1: argumentos en línea de comando
    if len(sys.argv) >= 3 and sys.argv[1] != '' and sys.argv[2] != '':
        return int(sys.argv[1]), int(sys.argv[2])

    # Caso 2: entrada estándar
    datos = sys.stdin.read().strip().split()
    if len(datos) >= 2:
        return int(datos[0]), int(datos[1])

    sys.exit(1)


a_orig, b_orig = leer_entrada()

gcd, x, y = euclides_extendido(a_orig, b_orig)

if gcd == 1:
    inverso = x % b_orig
    print(inverso)