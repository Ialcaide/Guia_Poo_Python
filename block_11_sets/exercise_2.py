import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Ejercicio 2 ------------------------------------------------------------
def exercise_2():
    clear()
    Display.header("Ejercicio 2 - Optimización: Eliminar Duplicados")
    
    my_list = [1, 2, 2, 3, 3, 3, 4]
    Display.row(f"Lista original con duplicados : {my_list}", FUCSIA)
    Display.empty()

    # Eliminación de duplicados convirtiendo a set y retornando a lista
    no_duplicates = list(set(my_list))

    Display.row(f"Estructura sin duplicados (list(set())) : {no_duplicates}", MORADO)
    Display.empty()
    Display.row("EXPLICACIÓN TÉCNICA:", FUCSIA)
    Display.row("La función nativa set() elimina los duplicados de forma automática", MORADO)
    Display.row("debido a que las colecciones hash de tipo conjunto (sets) no", MORADO)
    Display.row("permiten ni almacenan elementos repetidos en memoria.", MORADO)
    Display.footer()
