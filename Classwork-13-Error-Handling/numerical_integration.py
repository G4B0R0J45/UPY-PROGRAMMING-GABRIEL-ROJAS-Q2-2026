# Classwork 08 - Numerical Integration (version con manejo de errores para CW13)
# Declaracion de uso de IA: este codigo se elaboro con apoyo de IA (Claude, de
# Anthropic) para el manejo de errores, y fue revisado y probado contra todos
# los casos de prueba del autograder.

import math

# ------------------------------------------------------------
# Excepciones personalizadas (reglas de negocio - Unit III)
# Python NO detecta estos errores solo: se necesita raise
# ------------------------------------------------------------
class LimiteInvertidoError(Exception):
    pass

class MetodoInvalidoError(Exception):
    pass

# ------------------------------------------------------------
# INPUT: se lee todo como texto y despues se convierte
# ------------------------------------------------------------
a_str = input("Write the left endpoint of the interval: ")
b_str = input("Write the right endpoint of the interval: ")
f_x = input("Write the function to integrate: ").strip()
method = input("Select integration method (LRM/RRM/MPM/TM): ").strip()

# ------------------------------------------------------------
# PROCESS (con manejo de errores)
# ------------------------------------------------------------
try:
    # CASO 8: el limite inferior debe ser numerico
    # (float() / eval() lanzan la excepcion solos: ValueError, NameError, SyntaxError)
    try:
        if "pi" in a_str:
            a = eval(a_str.replace("pi", "math.pi"))
        else:
            a = float(a_str)
    except Exception:
        raise ValueError("El límite inferior debe ser numérico")

    # CASO 9: el limite superior debe ser numerico
    try:
        if "pi" in b_str:
            b = eval(b_str.replace("pi", "math.pi"))
        else:
            b = float(b_str)
    except Exception:
        raise ValueError("El límite superior debe ser numérico")

    # CASO 14 (regla de negocio): el intervalo no debe venir invertido
    if a >= b:
        raise LimiteInvertidoError("El límite inferior debe ser menor que el límite superior")

    # CASO 15 (regla de negocio): el metodo debe ser uno de los validos
    if method not in ("LRM", "RRM", "MPM", "TM"):
        raise MetodoInvalidoError("El método de integración no es válido. Usa LRM, RRM, MPM o TM")

    # CASOS 10, 11 y 12: probar la funcion en un punto antes de integrar
    x = (a + b) / 2  # punto de prueba dentro del intervalo
    try:
        eval(f_x)
    except NameError:
        # CASO 11: se uso una variable que no es x
        raise ValueError("La función debe estar escrita en términos de x")
    except ZeroDivisionError:
        # CASO 13: division entre cero, se atrapa abajo
        raise
    except Exception:
        # CASO 10 y 12: funcion vacia, "^" u otra sintaxis invalida
        raise ValueError("La función ingresada no es válida")

    # Integracion numerica (misma logica del CW08 original)
    area = 0.0
    n = 1000
    h = (b - a) / n
    shift = 0
    constant = 0.0

    if method == "RRM":
        shift = 1
    elif method == "MPM":
        constant = h / 2

    if method == "TM":
        # Trapezoid method
        for i in range(0, n + 1):
            xi = a + i * h
            x = xi
            height = eval(f_x)
            if i == 0 or i == n:
                area += height
            else:
                area += 2 * height
        area = area * h / 2
    else:
        # Rectangle methods (LRM, RRM, MPM)
        for i in range(0 + shift, n + shift):
            xi = a + i * h + constant
            x = xi
            height = eval(f_x)
            area += height * h

# ------------------------------------------------------------
# ERROR HANDLING: aqui se atrapan todas las excepciones
# ------------------------------------------------------------
except ZeroDivisionError:
    # CASO 13: Python detecta la division entre cero solo
    print("La función no está definida en algún punto del intervalo")
except (ValueError, LimiteInvertidoError, MetodoInvalidoError) as e:
    print(e)
except Exception:
    # Red de seguridad para cualquier otro error inesperado
    print("La función ingresada no es válida")
else:
    # ------------------------------------------------------------
    # OUTPUT: solo se imprime si no hubo ningun error
    # ------------------------------------------------------------
    print(f"The integration of {f_x} is {area:.3f}")
