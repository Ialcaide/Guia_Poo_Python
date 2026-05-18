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


class Navigator:

    WIDTH = 50

    @staticmethod
    def get_cols():
        return shutil.get_terminal_size((120, 40)).columns

    @staticmethod
    def pad(text: str) -> str:
        cols    = Navigator.get_cols()
        padding = (cols - Navigator.WIDTH) // 2
        return " " * padding + text

    @staticmethod
    def navigate(current: int, total: int, has_input: bool = False) -> int:
        w = Navigator.WIDTH

        print()
        # borde superior
        print(FUCSIA + Navigator.pad(TL + H * (w - 2) + TR) + RESET)

        # titulo
        title = "✦  NAVEGACION  ✦"
        print(FUCSIA + Navigator.pad(V) +
            FUCSIA + title.center(w - 2) +
            FUCSIA + V + RESET)

        # separador
        print(FUCSIA + Navigator.pad(TML + H * (w - 2) + TMR) + RESET)

        # espacio
        print(FUCSIA + Navigator.pad(V + " " * (w - 2) + V) + RESET)

        # opciones disponibles
        options = []
        if has_input:
            options.append("1.  Repetir ejercicio")
        if current > 1:
            options.append("2.  Ejercicio anterior")
        if current < total:
            options.append("3.  Siguiente ejercicio")
        options.append("4.  Ir a un ejercicio especifico")
        options.append("0.  Volver al menu")

        for opt in options:
            spaces = w - 2 - len(opt) - 3
            if spaces < 0:
                spaces = 1
            color = FUCSIA if opt.startswith("0") else MORADO
            print(FUCSIA + Navigator.pad(V) + "  " +
                color + opt + RESET +
                  " " * spaces +
                FUCSIA + V + RESET)
            print(FUCSIA + Navigator.pad(V + " " * (w - 2) + V) + RESET)

        # separador input
        print(FUCSIA + Navigator.pad(TML + H * (w - 2) + TMR) + RESET)

        # input dentro del marco
        prompt        = ">>>  Selecciona:  <<<"
        prompt_spaces = w - 2 - len(prompt) - 1
        print(FUCSIA + Navigator.pad(V) + " " +
            FUCSIA + prompt + RESET +
              " " * prompt_spaces +
            FUCSIA + V + RESET)

        # borde inferior
        print(FUCSIA + Navigator.pad(BL + H * (w - 2) + BR) + RESET)
        print()

        # input
        while True:
            cols    = Navigator.get_cols()
            padding = (cols - Navigator.WIDTH) // 2
            print(" " * (padding + 2), end="")
            try:
                choice = int(input(FUCSIA + "  Selecciona: " + RESET))
                if choice == 0:
                    return 0
                elif choice == 1 and has_input:
                    return current
                elif choice == 2 and current > 1:
                    return current - 1
                elif choice == 3 and current < total:
                    return current + 1
                elif choice == 4:
                    while True:
                        print(" " * (padding + 2), end="")
                        try:
                            print(FUCSIA + f"  Ejercicios disponibles 1 - {total}: " + RESET, end="")
                            target = int(input())
                            if 1 <= target <= total:
                                return target
                            print(" " * (padding + 2) +
                                FUCSIA + f"  Ingresa entre 1 y {total}" + RESET)
                        except ValueError:
                            print(" " * (padding + 2) +
                                FUCSIA + "  Invalido, ingresa un numero." + RESET)
                else:
                    print(" " * (padding + 2) +
                        FUCSIA + "  Opcion invalida." + RESET)
            except ValueError:
                print(" " * (padding + 2) +
                    FUCSIA + "  Invalido, ingresa un numero." + RESET)