"""
Classwork 12 – The Mandelbrot Set (Visualization)
Reads config.txt and mandelbrot.csv, maps iteration counts to pixel brightness,
and saves a PNG image.
"""

# ------------------------------------------------------------
# INPUT – Read config and CSV files
# ------------------------------------------------------------
from PIL import Image

config = {}

with open("config.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        parameter, value = line.strip().split("=")
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
# PROCESS – Create image from CSV data
# ------------------------------------------------------------
img = Image.new("HSV", (ancho, alto))

for linea in lineas:
    row, column, iterations = linea.strip().split(",")
    iterations = int(iterations)
    row = int(row)
    column = int(column)
    
    if iterations == max_iter:
        brightness = 0
    else:
        brightness = int((iterations / max_iter) * 255)
    
    img.putpixel((column, row), (brightness, 255, 255))

# ------------------------------------------------------------
# OUTPUT – Convert to RGB and save
# ------------------------------------------------------------
img_rgb = img.convert("RGB")
img_rgb.save("mandelbrot.png")
print("DONE")
