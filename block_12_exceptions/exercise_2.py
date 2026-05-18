import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def get_input_padding():
    cols = Display.get_cols()
    return " " * ((cols - Display.WIDTH) // 2 + 2)

# Ejercicio 2 ------------------------------------------------------------
def exercise_2():
    clear()
    Display.header("Ejercicio 2 - Captura Automatizada de IndexError")
    
    # Definimos la lista con 3 elementos (índices válidos: 0, 1 y 2)
    my_list = [10, 20, 30]
    
    Display.row(f"Lista definida en el código : {my_list}", FUCSIA)
    Display.row(f"Índices válidos disponibles  : 0, 1 y 2 (Largo: {len(my_list)})", MORADO)
    Display.empty()
    Display.row("Intentando acceder a un índice inexistente: my_list[5]...", MORADO)
    Display.empty()

    try:
        # Forzamos el error al pedir el índice 5 en una lista de largo 3
        valor = my_list[5]
        Display.row(f"Valor recuperado (No debería verse): {valor}", MORADO)
        
    except IndexError as error:
        # El bloque except atrapa el desborde de índice sin romper el programa
        Display.row("¡EXCEPCIÓN DE ÍNDICE ATRAPADA CON ÉXITO!", FUCSIA)
        Display.row("Error: el índice al que intentas acceder está fuera de rango.", FUCSIA)
        Display.empty()
        Display.row(f"Detalle técnico de Python: {error}", MORADO)
        
    Display.footer()
