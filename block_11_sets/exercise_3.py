import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Ejercicio 3 ------------------------------------------------------------
def exercise_3():
    clear()
    Display.header("Ejercicio 3 - Álgebra de Conjuntos Combinada")
    
    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}

    union        = A | B
    interseccion = A & B
    resultado    = union - interseccion

    Display.row(f"Conjunto A = {A}  |  Conjunto B = {B}", FUCSIA)
    Display.empty()
    Display.row(f"1. Unión        (A | B) = {union}", MORADO)
    Display.row(f"2. Intersección (A & B) = {interseccion}", MORADO)
    Display.row(f"3. Diferencia   (1 - 2) = {resultado}", FUCSIA)
    Display.empty()
    
    Display.row("ANÁLISIS COMPARATIVO:", FUCSIA)
    Display.row("El resultado contiene los elementos que pertenecen de forma aislada", MORADO)
    Display.row("a los conjuntos, descartando aquellos que comparten entre sí.", MORADO)
    Display.row("Esta lógica equivale exactamente a la Diferencia Simétrica (^).", MORADO)
    Display.empty()
    Display.row(f"Comprobación directa -> A ^ B = {A ^ B}", FUCSIA)
    Display.footer()

