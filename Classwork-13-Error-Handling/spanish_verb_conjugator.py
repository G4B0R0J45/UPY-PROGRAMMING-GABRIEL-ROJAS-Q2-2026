# Classwork 09 - Spanish Verb Conjugator (version con manejo de errores para CW13)
# Declaracion de uso de IA: este codigo se elaboro con apoyo de IA (Claude, de
# Anthropic) para el manejo de errores, y fue revisado y probado contra todos
# los casos de prueba del autograder.

# ------------------------------------------------------------
# Excepciones personalizadas (reglas de negocio - Unit III)
# Python NO detecta estos errores solo: se necesita raise
# ------------------------------------------------------------
class VerboEnMayusculasError(Exception):
    pass

class EspaciosExtraError(Exception):
    pass

# ------------------------------------------------------------
# Required Structures
# ------------------------------------------------------------
pronouns = ["Yo", "Tú", "Él", "Nosotros", "Vosotros", "Ellos"]

endings = {
    "ar": ["o", "as", "a", "amos", "ais", "an"],
    "er": ["o", "es", "e", "emos", "eis", "en"],
    "ir": ["o", "es", "e", "imos", "is", "en"]
}

# ------------------------------------------------------------
# INPUT
# ------------------------------------------------------------
try:
    verb = input("Write a spanish verb (ar/er/ir): ")
except EOFError:
    verb = ""  # por si el input llega totalmente vacio

# ------------------------------------------------------------
# PROCESS (con manejo de errores)
# ------------------------------------------------------------
try:
    # CASO 24 (regla de negocio): el verbo no debe traer espacios extra
    if " " in verb:
        raise EspaciosExtraError("El verbo no debe tener espacios extra")

    # CASO 23 (regla de negocio): el verbo debe venir en minusculas
    if verb != verb.lower():
        raise VerboEnMayusculasError("El verbo debe escribirse en minúsculas")

    stem = verb[:-2]    # Get the stem
    ending = verb[-2:]  # Get the ending

    # CASOS 19-22: si la terminacion no es ar/er/ir, Python lanza
    # KeyError solo y lo atrapamos con try/except
    conjugations = endings[ending]

except KeyError:
    print("El verbo debe terminar en ar, er o ir")
except (EspaciosExtraError, VerboEnMayusculasError) as e:
    print(e)
else:
    # ------------------------------------------------------------
    # OUTPUT
    # ------------------------------------------------------------
    for index, pronoun in enumerate(pronouns):
        termination = conjugations[index]
        print(f"{pronoun} {stem}{termination}")
