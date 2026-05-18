from blocks.block_01_constructor.exercise_1 import exercise_1
from blocks.block_01_constructor.exercise_2 import exercise_2
from blocks.block_01_constructor.exercise_3 import exercise_3
from core.navigator import Navigator
from menu.menu import Menu

# Menú-----------------------------------------------------------------
def run_menu():
    block_menu = Menu("BLOQUE 11 - CONJUNTOS", [
        "Ejercicio 1 - Unión, intersección y diferencia",
        "Ejercicio 2 - Eliminar duplicados de una lista",
        "Ejercicio 3 - Operaciones combinadas: (A|B) - (A&B)",
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
            current_exercise = Navigator.navigate(3, 3, has_input=False)

        if current_exercise == 0:
            current_exercise = None