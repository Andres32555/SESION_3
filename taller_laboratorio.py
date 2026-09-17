"""
Sesion 3 - Taller de Laboratorio: Logica Difusa Comercial (40 MIN)
Evaluacion de la "Experiencia" de un conductor mediante 3 conjuntos difusos.
"""


# Paso 1: funcion de membresia triangular (implementacion computacional)
def membresia_triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0.0
    elif a < x <= b:
        return (x - a) / (b - a)
    elif b < x < c:
        return (c - x) / (c - b)


# Conjuntos difusos de "Experiencia" (vertices a, b, c)
CONJUNTOS = {
    "novato": (0, 0, 5),
    "intermedio": (2, 5, 8),
    "experto": (5, 10, 20),
}

# Paso 2: conductores a evaluar
conductores = [3, 6, 12]

# Paso 3 y 4: calculo de grados de membresia + categoria dominante (max)
if __name__ == "__main__":
    for anios in conductores:
        grados = {
            nombre: membresia_triangular(anios, *vertices)
            for nombre, vertices in CONJUNTOS.items()
        }

        categoria = max(grados, key=grados.get)

        print(f"Conductor con {anios} años de experiencia:")
        for nombre, grado in grados.items():
            print(f"  - {nombre}: {grado:.2f}")
        print(f"  => Categoría dominante: {categoria.upper()} (grado {grados[categoria]:.2f})\n")
