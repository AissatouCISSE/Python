# Import ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from math import pi

# Programme principal =========================================================
rayon = float(input("Rayon du cercle (m) :"))
surface = pi*(rayon*rayon)
Périmètre = rayon * 2 * pi
print("La surface du cercle est", surface)
print("Le périmètre du cercle est : ", Périmètre)