import os
import shutil
import colorama
from colorama import Style

colorama.init()

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = Style.RESET_ALL

TL  = "╔"
TR  = "╗"
BL  = "╚"
BR  = "╝"
H   = "═"
V   = "║"
TML = "╠"
TMR = "╣"


class Menu:

    WIDTH = 70

    def __init__(self, title: str, options: list):
        self.title   = title
        self.options = options

    def clear_screen(self):
        os.system("cls" if os.name == "nt" else "clear")

    def get_cols(self):
        return shutil.get_terminal_size((120, 40)).columns

    def pad(self, text: str) -> str:
        cols    = self.get_cols()
        padding = (cols - self.WIDTH) // 2
        return " " * padding + text

    def display(self):
        self.clear_screen()
        w = self.WIDTH

        print()

        # borde superior
        print(FUCSIA + self.pad(TL + H * (w - 2) + TR) + RESET)

        # titulo MENU DE OPCIONES
        title = "✦  MENU DE OPCIONES  ✦"
        inner = title.center(w - 2)
        print(FUCSIA + self.pad(V) + FUCSIA + inner + FUCSIA + V + RESET)

        # separador
        print(FUCSIA + self.pad(TML + H * (w - 2) + TMR) + RESET)

        # titulo del bloque
        block = self.title.center(w - 2)
        print(FUCSIA + self.pad(V) + MORADO + block + RESET + FUCSIA + V + RESET)

        # separador
        print(FUCSIA + self.pad(TML + H * (w - 2) + TMR) + RESET)

        # espacio
        print(FUCSIA + self.pad(V + " " * (w - 2) + V) + RESET)

        # opciones
        for i, option in enumerate(self.options, 1):
            opt_text = f"  {i}.  {option}"
            spaces   = w - 2 - len(opt_text) - 1
            if spaces < 0:
                spaces = 1
            print(FUCSIA + self.pad(V) + " " +
                MORADO + opt_text + RESET +
                  " " * spaces +
                FUCSIA + V + RESET)
            print(FUCSIA + self.pad(V + " " * (w - 2) + V) + RESET)

        # separador exit
        print(FUCSIA + self.pad(TML + H * (w - 2) + TMR) + RESET)

        # exit/back
        exit_label = "Exit" if "Menu" in self.title else "Salir"
        exit_text  = f"  0.  {exit_label}"
        exit_spaces = w - 2 - len(exit_text) - 1
        print(FUCSIA + self.pad(V) + " " +
            FUCSIA + exit_text + RESET +
              " " * exit_spaces +
            FUCSIA + V + RESET)

        # separador input
        print(FUCSIA + self.pad(TML + H * (w - 2) + TMR) + RESET)

        # input dentro del marco
        prompt      = ">>>  Selecciona una opcion:  <<<"
        prompt_spaces = w - 2 - len(prompt) - 1
        print(FUCSIA + self.pad(V) + " " +
            FUCSIA + prompt + RESET +
              " " * prompt_spaces +
            FUCSIA + V + RESET)

        # borde inferior
        print(FUCSIA + self.pad(BL + H * (w - 2) + BR) + RESET)
        print()

    def get_choice(self) -> int:
        cols    = self.get_cols()
        padding = (cols - self.WIDTH) // 2

        while True:
            try:
                print(" " * (padding + 2), end="")
                choice = int(input(FUCSIA + "  Selecciona: " + RESET))
                if 0 <= choice <= len(self.options):
                    return choice
                print(" " * (padding + 2) +
                    FUCSIA + f"  Ingresa entre 0 y {len(self.options)}" + RESET)
            except ValueError:
                print(" " * (padding + 2) +
                    FUCSIA + "  Invalido, ingresa un numero." + RESET)