"""
Classwork 11 – The Mandelbrot Set
Computes the Mandelbrot set by reading a config file, iterating over
each pixel, and saving the iteration counts to a CSV file.
"""

# ------------------------------------------------------------
# INPUT – Read config file
# ------------------------------------------------------------
config = {}

with open("config.txt", "r", encoding="utf-8") as file:
    for line in file:
        parameter, value = line.strip().split("=")
        config[parameter] = float(value) if "." in value else int(value)

# ------------------------------------------------------------
# PROCESS – Compute Mandelbrot set and write to CSV
# ------------------------------------------------------------
width = int(config["ancho"])
height = int(config["alto"])
max_iter = int(config["max_iter"])

with open("mandelbrot.csv", "w", encoding="utf-8") as output:
    output.write("row,column,iterations\n")
    
    for row in range(height):
        for column in range(width):
            real = config["real_min"] + (column / width) * (config["real_max"] - config["real_min"])
            imag = config["imag_min"] + (row / height) * (config["imag_max"] - config["imag_min"])
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
