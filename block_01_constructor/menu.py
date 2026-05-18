from blocks.block_01_constructor.exercise_1 import exercise_1
from blocks.block_01_constructor.exercise_2 import exercise_2
from blocks.block_01_constructor.exercise_3 import exercise_3
from blocks.block_01_constructor.exercise_4 import exercise_4
from core.navigator import Navigator
from menu.menu import Menu


def run_menu():
    block_menu = Menu("Bloque 1 - Constructor", [
        "Ejercicio 1 - Instancia 2 productos",
        "Ejercicio 2 - Validación precio negativo",
        "Ejercicio 3 - Crear estudiante con nombre y notas",
        "Ejercicio 4 - Método de clase (classmethod)",
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
            current_exercise = Navigator.navigate(1, 4, has_input=False)
        elif current_exercise == 2:
            exercise_2()
            current_exercise = Navigator.navigate(2, 4, has_input=False)
        elif current_exercise == 3:
            exercise_3()
            current_exercise = Navigator.navigate(3, 4, has_input=False)
        elif current_exercise == 4:
            exercise_4()
            current_exercise = Navigator.navigate(4, 4, has_input=False)

        if current_exercise == 0:
            current_exercise = None