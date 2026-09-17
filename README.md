# Sesión 3 — Incertidumbre y Lógica Difusa

## Taller Analítico 1: Cálculo de Grados de Verdad (20 min)

**Conjunto difuso "Temperatura Agradable"** (función triangular, vértices `a=18°C, b=22°C, c=26°C`):


μ(x) = 0,               si x <= a
μ(x) = (x - a) / (b - a), si a < x <= b
μ(x) = (c - x) / (c - b), si b < x < c
μ(x) = 0,               si x > c


### Paso 1 — x = 20°C (rampa de subida, a < x <= b)

`μ(20) = (20 - 18) / (22 - 18) = 2 / 4 = 0.5`

### Paso 2 — x = 25°C (rampa de bajada, b < x < c)

`μ(25) = (26 - 25) / (26 - 22) = 1 / 4 = 0.25`

### Paso 3 — Interpretación

- `μ(20) = 0.5`: a 20°C la oficina pertenece al conjunto "Temperatura Agradable" en un **50%**, es decir, está a mitad de camino subiendo hacia el punto de mayor confort (22°C, μ=1.0).
- `μ(25) = 0.25`: a 25°C la pertenencia es **menor (25%)** porque ya se está bajando por el lado derecho del triángulo, acercándose al límite (26°C, μ=0).
- Estos números entre 0 y 1 le dicen al motor de inferencia **cuánta verdad** tiene la premisa "la temperatura es agradable", permitiendo activar reglas incluso cuando la temperatura no es exactamente el valor ideal, a diferencia de la lógica booleana estricta.

---

## Taller de Laboratorio: Lógica Difusa Comercial (40 min)

**Misión práctica:** evaluar la "Experiencia" de un conductor según sus años trabajados, con 3 conjuntos difusos:

- **Novato:** triángulo `(0, 0, 5)`
- **Intermedio:** triángulo `(2, 5, 8)`
- **Experto:** triángulo `(5, 10, 20)`

1. Implementar `membresia_triangular`.
2. Ciclo `for` que evalúa 3 conductores: `[3, 6, 12]` años.
3. Para cada conductor, calcular e imprimir sus 3 grados de membresía (novato, intermedio, experto).
4. Determinar algorítmicamente (con `max()`) en qué categoría encaja mejor cada conductor.

