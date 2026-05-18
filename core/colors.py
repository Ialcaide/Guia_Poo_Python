import colorama
from colorama import Fore, Style

colorama.init()


class Color:

    # colores de texto
    CYAN    = Fore.CYAN
    YELLOW  = Fore.YELLOW
    GREEN   = Fore.GREEN
    RED     = Fore.RED
    WHITE   = Fore.WHITE
    BLUE    = Fore.BLUE
    MAGENTA = Fore.MAGENTA

    # estilos
    BOLD    = Style.BRIGHT
    RESET   = Style.RESET_ALL

    @staticmethod
    def cyan(text: str) -> str:
        return f"{Fore.CYAN}{text}{Style.RESET_ALL}"

    @staticmethod
    def yellow(text: str) -> str:
        return f"{Fore.YELLOW}{text}{Style.RESET_ALL}"

    @staticmethod
    def green(text: str) -> str:
        return f"{Fore.GREEN}{text}{Style.RESET_ALL}"

    @staticmethod
    def red(text: str) -> str:
        return f"{Fore.RED}{text}{Style.RESET_ALL}"

    @staticmethod
    def white(text: str) -> str:
        return f"{Fore.WHITE}{text}{Style.RESET_ALL}"

    @staticmethod
    def blue(text: str) -> str:
        return f"{Fore.BLUE}{text}{Style.RESET_ALL}"

    @staticmethod
    def magenta(text: str) -> str:
        return f"{Fore.MAGENTA}{text}{Style.RESET_ALL}"

    @staticmethod
    def bold(text: str) -> str:
        return f"{Style.BRIGHT}{text}{Style.RESET_ALL}"