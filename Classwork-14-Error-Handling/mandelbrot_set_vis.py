"""
Classwork 12 - The Mandelbrot Set (Visualization)
Reads config.txt and mandelbrot.csv, maps iteration counts to pixel
brightness, and saves a grayscale PNG image.

Classwork 14 - Error Handling added:
- Python-detected errors are caught with try/except:
  FileNotFoundError (missing config.txt or mandelbrot.csv),
  ValueError (a malformed CSV row) and IndexError (a CSV coordinate
  outside the width/height declared in config.txt).
"""

# ============================================================
# DECLARACION DE USO DE IA
# IA utilizada: Claude (Anthropic)
# Fecha: 17 de julio de 2026
# Proposito: Agregar manejo de errores (Unidad III) al programa
#            original, atrapando con try/except los errores que
#            Python detecta cuando faltan archivos o cuando el
#            mandelbrot.csv no es consistente con el config.txt.
# ============================================================

from PIL import Image

try:
    # ------------------------------------------------------------
    # INPUT - Read config and CSV files
    # ------------------------------------------------------------
    config = {}
    with open("config.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line == "":
                continue
            parameter, value = line.split("=")
            config[parameter] = float(value) if "." in value else int(value)

    with open("mandelbrot.csv", "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    # Remove header row
    lineas.pop(0)

    # Unpack variables
    max_iter = config["max_iter"]
    ancho = int(config["ancho"])
    alto = int(config["alto"])

    # ------------------------------------------------------------
    # PROCESS - Create image from CSV data
    # ------------------------------------------------------------
    img = Image.new("L", (ancho, alto))
    for linea in lineas:
        linea = linea.strip()
        if linea == "":
            continue
        # ValueError if a CSV row does not have exactly row,column,iterations
        row, column, iterations = linea.split(",")
        iterations = int(iterations)
        row = int(row)
        column = int(column)

        if iterations == max_iter:
            brightness = 0
        else:
            brightness = int((iterations / max_iter) * 255)

        # IndexError if column/row fall outside the image size
        img.putpixel((column, row), brightness)

    # ------------------------------------------------------------
    # OUTPUT - Save the image
    # ------------------------------------------------------------
    img.save("mandelbrot.png")
    print("DONE")

except FileNotFoundError as missing:
    print(f"No se encontró el archivo {missing.filename}")
except ValueError:
    print("El archivo mandelbrot.csv está mal formado: cada fila debe tener row,column,iterations.")
except IndexError:
    print("El mandelbrot.csv no es consistente con el ancho/alto del config.txt.")
