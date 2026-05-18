from menu.menu import Menu
from blocks.block_00_intro.menu          import run_menu as block0
from blocks.block_01_constructor.menu    import run_menu as block1
from blocks.block_02_variables.menu      import run_menu as block2
from blocks.block_03_operators.menu      import run_menu as block3
from blocks.block_04_input_output.menu   import run_menu as block4
from blocks.block_05_conditionals.menu   import run_menu as block5
from blocks.block_06_loops.menu          import run_menu as block6
from blocks.block_07_functions.menu      import run_menu as block7
from blocks.block_08_lists.menu          import run_menu as block8
from blocks.block_09_tuples.menu         import run_menu as block9
from blocks.block_10_dictionaries.menu   import run_menu as block10
from blocks.block_11_sets.menu           import run_menu as block11
from blocks.block_12_exceptions.menu     import run_menu as block12
from blocks.block_13_decorators.menu     import run_menu as block13
from blocks.block_14_unpacking.menu      import run_menu as block14
from blocks.block_15_higher_order.menu   import run_menu as block15
from blocks.block_16_files_json.menu     import run_menu as block16
from blocks.block_17_mixins.menu         import run_menu as block17
from blocks.exercises_AI                 import run_menu as block_extra


class App:

    def __init__(self):
        self.menu = Menu("Bienvenido al menu de opciones", [
            "Bloque 00 - Intro a la POO",
            "Bloque 01 - Constructor",
            "Bloque 02 - Variables",
            "Bloque 03 - Operadores",
            "Bloque 04 - Entrada y Salida",
            "Bloque 05 - Condicionales",
            "Bloque 06 - Bucles (Loops)",
            "Bloque 07 - Funciones",
            "Bloque 08 - Listas",
            "Bloque 09 - Tuplas",
            "Bloque 10 - Diccionarios",
            "Bloque 11 - Conjuntos (Sets)",
            "Bloque 12 - Excepciones",
            "Bloque 13 - Decoradores",
            "Bloque 14 - Desempaquetado (Unpacking)",
            "Bloque 15 - Funciones de Orden Superior",
            "Bloque 16 - Archivos y JSON",
            "Bloque 17 - Mixins",
            "Ejercicios Extra - IA",
        ])

        self.blocks = {
            1 : block0,
            2 : block1,
            3 : block2,
            4 : block3,
            5 : block4,
            6 : block5,
            7 : block6,
            8 : block7,
            9 : block8,
            10: block9,
            11: block10,
            12: block11,
            13: block12,
            14: block13,
            15: block14,
            16: block15,
            17: block16,
            18: block17,
            19: block_extra,
        }

    def run(self):
        while True:
            self.menu.display()
            choice = self.menu.get_choice()

            if choice == 0:
                print("Goodbye!")
                break

            block = self.blocks.get(choice)
            if block:
                block()


app = App()
app.run()