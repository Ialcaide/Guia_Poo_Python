from blocks.block_01_constructor.exercise_1 import exercise_1
from blocks.block_01_constructor.exercise_2 import exercise_2
from blocks.block_01_constructor.exercise_3 import exercise_3
from core.navigator import Navigator
from menu.menu import Menu

# Menú Principal ------------------------------------------------------------

def run_menu():
    block_menu = Menu("BLOQUE 16 - ARCHIVOS Y JSON", [
        "Ejercicio 1 - Escribir y leer archivo plano",
        "Ejercicio 2 - Guardar y cargar JSON básico",
        "Ejercicio 3 - Lista de usuarios en JSON",
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
            current_exercise = Navigator.navigate(1, 3, has_input=True)
        elif current_exercise == 2:
            exercise_2()
            current_exercise = Navigator.navigate(2, 3, has_input=True)
        elif current_exercise == 3:
            exercise_3()
            current_exercise = Navigator.navigate(3, 3, has_input=True)

        if current_exercise == 0:
            current_exercise = None