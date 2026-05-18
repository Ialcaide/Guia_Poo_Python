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
    Display.header("Ejercicio 3 - Gestión de Memoria: Referencia vs Copia")
    
# estado inicial
    data           = {"a": 1}
    reference_copy = data
    real_copy      = data.copy()

# Mutacion
    reference_copy["b"] = 2

    Display.row("DECLARACIÓN ORIGINAL:", FUCSIA)
    Display.row("data = {'a': 1}", MORADO)
    Display.row("reference_copy = data        (Apunta al mismo objeto)", MORADO)
    Display.row("real_copy = data.copy()      (Crea un objeto nuevo aislado)", MORADO)
    Display.empty()
    
    Display.row("ESTADO POST-MUTACIÓN [ reference_copy['b'] = 2 ]:", FUCSIA)
    Display.empty()
    Display.row(f"data           : {data}", MORADO)
    Display.row(f"reference_copy : {reference_copy}", MORADO)
    Display.row(f"real_copy      : {real_copy}", MORADO)
    Display.footer()
