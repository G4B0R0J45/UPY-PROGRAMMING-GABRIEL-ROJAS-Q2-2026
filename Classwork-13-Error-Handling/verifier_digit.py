# Classwork 07 - Verifier Digit (version con manejo de errores para CW13)
# Declaracion de uso de IA: este codigo se elaboro con apoyo de IA (Claude, de
# Anthropic) para el manejo de errores, y fue revisado y probado contra todos
# los casos de prueba del autograder.

# ------------------------------------------------------------
# Excepcion personalizada (Unit III)
# ------------------------------------------------------------
class DigitoApocrifoError(Exception):
    pass

# ------------------------------------------------------------
# INPUT
# ------------------------------------------------------------
rol = input("Escribe el rol (ejemplo: 20261234-5): ").strip()

# ------------------------------------------------------------
# PROCESS (validaciones + calculo del digito verificador)
# ------------------------------------------------------------
# CASO 1 y 2: el rol debe tener exactamente un guion
if rol.count("-") != 1:
    print("Rol inválido: No tiene el formato XXXXXXXXX-X")

else:
    rol_sin_digito, digito = rol.split("-")

    # CASO 3: la parte antes del guion debe ser numerica
    if not rol_sin_digito.isdigit():
        print("Los digitos del rol deben ser numéricos")

    # CASO 4: la parte despues del guion debe ser numerica
    elif not digito.isdigit():
        print("El digito verificador debe ser numérico")

    else:
        inverso = rol_sin_digito[::-1]
        secuencia = [2, 3, 4, 5, 6, 7]
        suma = 0

        for index in range(len(inverso)):
            numero = int(inverso[index])
            suma += numero * secuencia[index % 6]

        resultado = suma % 11
        verificador = 11 - resultado

        # ------------------------------------------------------------
        # ERROR HANDLING (Unit III: raise + try/except/else)
        # ------------------------------------------------------------
        try:
            # CASO 5: regla de negocio -> Python no la detecta solo, necesita raise
            if verificador != int(digito):
                raise DigitoApocrifoError(f"Error: El dígito verificador no conicide, se esperaba {verificador}")
        except DigitoApocrifoError as e:
            print(e)
        else:
            # ------------------------------------------------------------
            # OUTPUT
            # ------------------------------------------------------------
            # CASO 6 y 7: el digito coincide -> se imprime el rol validado
            print(f"{rol_sin_digito}-{digito}")
