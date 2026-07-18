"""
Classwork 11 - The Mandelbrot Set
Computes the Mandelbrot set by reading a config file, iterating over
each pixel, and saving the iteration counts to a CSV file.

Classwork 14 - Error Handling added:
- Python-detected errors are caught with try/except:
  FileNotFoundError (missing config.txt), ValueError (a line without "="),
  KeyError (a required parameter is missing) and TypeError ("ancho"/"alto"
  given as a decimal number instead of an integer).
"""

# ============================================================
# DECLARACION DE USO DE IA
# IA utilizada: Claude (Anthropic)
# Fecha: 17 de julio de 2026
# Proposito: Agregar manejo de errores (Unidad III) al programa
#            original, atrapando con try/except los errores que
#            Python detecta al leer un config.txt mal formado o
#            incompleto.
# ============================================================

try:
    # ------------------------------------------------------------
    # INPUT - Read config file
    # ------------------------------------------------------------
    config = {}
    with open("config.txt", "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            # ValueError if a line does not have the format parameter=value
            parameter, value = line.split("=")
            config[parameter] = float(value) if "." in value else int(value)

    # KeyError if any required parameter is missing from config.txt
    width = config["ancho"]
    height = config["alto"]
    max_iter = config["max_iter"]
    real_min = config["real_min"]
    real_max = config["real_max"]
    imag_min = config["imag_min"]
    imag_max = config["imag_max"]

    # ------------------------------------------------------------
    # PROCESS - Compute Mandelbrot set and write to CSV
    # ------------------------------------------------------------
    with open("mandelbrot.csv", "w", encoding="utf-8") as output:
        output.write("row,column,iterations\n")

        # TypeError if "ancho"/"alto" are floats (e.g. 4.0) instead of ints
        for row in range(height):
            for column in range(width):
                real = real_min + (column / width) * (real_max - real_min)
                imag = imag_min + (row / height) * (imag_max - imag_min)
                c = complex(real, imag)

                z = 0 + 0j
                iterations = 0

                while (abs(z) <= 2) and (iterations < max_iter):
                    z = z * z + c
                    iterations += 1

                output.write(f"{row},{column},{iterations}\n")

    # ------------------------------------------------------------
    # OUTPUT
    # ------------------------------------------------------------
    print("Done!")

except FileNotFoundError:
    print("No se encontró el archivo config.txt")
except ValueError:
    print("El archivo config.txt está mal formado: cada línea debe tener el formato parametro=valor.")
except KeyError as missing:
    print(f"Falta el parámetro {missing} en config.txt")
except TypeError:
    print("Los parámetros 'ancho' y 'alto' deben ser números enteros.")
