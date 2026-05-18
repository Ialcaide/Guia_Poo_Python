import shutil
import colorama
from colorama import Style

colorama.init()

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
VERDE  = "\033[38;2;0;255;150m"
RESET  = Style.RESET_ALL

TL  = "╔"
TR  = "╗"
BL  = "╚"
BR  = "╝"
H   = "═"
V   = "║"
TML = "╠"
TMR = "╣"

COLS = 120
ROWS = 40


class Display:

    WIDTH = 85

    @staticmethod
    def gotoxy(x: int, y: int):
        print(f"\033[{y};{x}H", end="", flush=True)

    @staticmethod
    def get_cols():
        return shutil.get_terminal_size((120, 40)).columns

    @staticmethod
    def pad(text: str) -> str:
        cols    = Display.get_cols()
        padding = (cols - Display.WIDTH) // 2
        return " " * padding + text

    @staticmethod
    def header(title: str):
        w = Display.WIDTH
        print()
        print(FUCSIA + Display.pad(TL + H * (w - 2) + TR) + RESET)
        inner = f"✦  {title}  ✦"
        print(FUCSIA + Display.pad(V) +
            FUCSIA + inner.center(w - 2) +
            FUCSIA + V + RESET)
        print(FUCSIA + Display.pad(TML + H * (w - 2) + TMR) + RESET)
        print(FUCSIA + Display.pad(V + " " * (w - 2) + V) + RESET)

    @staticmethod
    def row(text: str, color: str = ""):
        w      = Display.WIDTH
        spaces = w - 2 - len(text) - 3
        if spaces < 0:
            spaces = 1
        print(FUCSIA + Display.pad(V) + "  " +
            color + text + RESET +
              " " * spaces +
            FUCSIA + V + RESET)

    @staticmethod
    def empty():
        w = Display.WIDTH
        print(FUCSIA + Display.pad(V + " " * (w - 2) + V) + RESET)

    @staticmethod
    def separator():
        w = Display.WIDTH
        print(FUCSIA + Display.pad(TML + H * (w - 2) + TMR) + RESET)

    @staticmethod
    def footer():
        w = Display.WIDTH
        print(FUCSIA + Display.pad(V + " " * (w - 2) + V) + RESET)
        print(FUCSIA + Display.pad(BL + H * (w - 2) + BR) + RESET)
        print()

    @staticmethod
    def input_at(prompt: str) -> str:
        # usa gotoxy para posicionar el cursor
        cols    = Display.get_cols()
        x       = (cols - Display.WIDTH) // 2 + 4
        y       = ROWS - 4
        Display.gotoxy(x, y)
        return input(FUCSIA + f"  {prompt} " + RESET)

    @staticmethod
    def input_row(prompt: str) -> str:
        w             = Display.WIDTH
        cols          = Display.get_cols()
        padding       = (cols - w) // 2
        Display.separator()
        prompt_spaces = w - 2 - len(prompt) - 1
        print(FUCSIA + Display.pad(V) + " " +
            FUCSIA + prompt + RESET +
              " " * prompt_spaces +
            FUCSIA + V + RESET)
        Display.footer()
        # usa gotoxy para posicionar el cursor del input
        x = padding + 4
        y = ROWS - 4
        Display.gotoxy(x, y)
        return input(FUCSIA + f"  {prompt} " + RESET)