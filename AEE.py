def euclides_extendido(a, b):
    intercambiado = False

    # Tu lógica original de swap
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
        
    # Si hubo intercambio, regresamos los coeficientes cruzados
    if intercambiado:
        return a, y0, x0
    else:
        return a, x0, y0

# --- Cambios en la entrada y lógica de salida ---

# Pedimos específicamente el número y el módulo
a_orig = int(input("Dame el número del que quieres saber el inverso: "))
b_orig = int(input("Bajo qué módulo: "))

gcd, x, y = euclides_extendido(a_orig, b_orig)

# 1. Verificación obligatoria: el inverso solo existe si el gcd es 1
if gcd != 1:
    print(f"\nEl inverso no existe porque el gcd({a_orig}, {b_orig}) = {gcd}")
else:
    # 2. El inverso es 'x' porque es el que acompaña al primer valor ingresado (a_orig)
    inverso = x
    
    # 3. Consideración por si el inverso es negativo: sumarle el módulo
    if inverso < 0:
        inverso = inverso + b_orig
        
    print(f"\nEl inverso de {a_orig} mod {b_orig} es: {inverso}")
    print(f"Verificación: ({a_orig} * {inverso}) % {b_orig} = {(a_orig * inverso) % b_orig}")