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

if len(sys.argv) != 3:
    sys.exit(1)

a_orig = int(sys.argv[1])
b_orig = int(sys.argv[2])

gcd, x, y = euclides_extendido(a_orig, b_orig)

if gcd == 1:
    inverso = x
    if inverso < 0:
        inverso = inverso + b_orig
    print(inverso)