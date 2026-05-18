from blocks.block_01_constructor.exercise_1 import exercise_1
from blocks.block_01_constructor.exercise_2 import exercise_2
from blocks.block_01_constructor.exercise_3 import exercise_3
from core.navigator import Navigator
from menu.menu import Menu

# Menu----------------------------------------------------
def run_menu():
    block_menu = Menu("BLOQUE 03 - OPERADORES", [
        "Ejercicio 1 - Operadores Aritméticos",
        "Ejercicio 2 - Comparación Léxica (== vs is)",
        "Ejercicio 3 - Precedencia y Jerarquía de Operadores",
    ])

    current_exercise = None

    while True:
        if current_exercise is None:
            block_menu.display()
            choice = block_menu.get_choice()
            if choice == 0:
                break
            else:
                current_exercise = choice

        if current_exercise == 1:
            exercise_1()
            current_exercise = Navigator.navigate(1, 3, has_input=False)
        elif current_exercise == 2:
            exercise_2()
            current_exercise = Navigator.navigate(2, 3, has_input=False)
        elif current_exercise == 3:
            exercise_3()
            # Al regresar del interactivo del Ejercicio 3, volvemos al menú principal
            current_exercise = None 

        if current_exercise == 0:
            current_exercise = None