import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Ejercicio 3-------------------------------------------------
def exercise_3():
    clear()
    Display.header("Ejercicio 3 - Manejo de Memoria: Referencia vs Copia")
    
    # Lista base original
    my_list = [1, 2, 3]

    # Copia por referencia - apunta exactamente al mismo objeto id()
    reference_copy = my_list

    # Copia real - reserva una nueva sección y objeto en memoria
    real_copy = my_list.copy()

    # Operación de mutación sobre la copia referencial
    reference_copy.append(4)

    Display.row("DECLARACIÓN DE ASIGNACIONES:", FUCSIA)
    Display.row("reference_copy = my_list  (Mismo puntero / referencia)", MORADO)
    Display.row("real_copy = my_list.copy() (Nueva instancia de objeto)", MORADO)
    Display.empty()
    
    Display.row("EVALUACIÓN POST MUTACIÓN [ reference_copy.append(4) ]:", FUCSIA)
    Display.empty()
    Display.row(f"my_list         : {my_list}", MORADO)
    Display.row(f"reference_copy  : {reference_copy}", MORADO)
    Display.row(f"real_copy       : {real_copy}", MORADO)
    Display.empty()
    
    Display.row("ANÁLISIS TÉCNICO EXPLICATIVO:", FUCSIA)
    Display.row("La lista base 'my_list' se vio alterada debido a que 'reference_copy'", MORADO)
    Display.row("comparte exactamente la misma dirección lógica del objeto original.", MORADO)
    Display.row("'real_copy' permaneció intacta gracias a que la función .copy()", MORADO)
    Display.row("clona los datos aislando la estructura en un bloque nuevo.", MORADO)
    Display.footer()
