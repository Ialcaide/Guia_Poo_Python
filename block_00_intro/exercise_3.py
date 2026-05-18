import os
from core.display import Display

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")
# Ejercicio 3 ----------------------------------------------------------------------------------------------------------
def exercise_3():
    clear()
    Display.header("Ejercicio 3 - Clase vs Objeto")
    Display.row("¿Que es una clase?", FUCSIA)
    Display.empty()
    Display.row("Es un tipo de dato definido por el programador.", MORADO)
    Display.row("Es una estructura logica que agrupa atributos y metodos.", MORADO)
    Display.empty()
    Display.row("¿Que es un objeto?", FUCSIA)
    Display.empty()
    Display.row("Es una instancia de esa clase.", MORADO)
    Display.row("Contiene valores especificos y ejecuta los metodos.", MORADO)
    Display.empty()
    Display.row("Diferencia clave:", FUCSIA)
    Display.empty()
    Display.row("Clase  → es el QUE ES (la estructura)", MORADO)
    Display.row("Objeto → es el QUIEN ES (la entidad con datos propios)", MORADO)
    Display.footer()

    # minijuego
    Display.header("PRUEBA LO APRENDIDO")
    Display.row("escribe 'salir' en cualquier momento para terminar", FUCSIA)
    Display.footer()

    puntos = 0
    total_respondidas = 0
    desafios = [
        {"pregunta": "1. El plano de un Ferrari rojo:", "respuesta": "clase"},
        {"pregunta": "2. El perro 'Bobby' que ladra en tu jardin:", "respuesta": "objeto"},
        {"pregunta": "3. La receta secreta de una pizza:", "respuesta": "clase"},
        {"pregunta": "4. El iPhone 15 con numero de serie SN-999:", "respuesta": "objeto"}
    ]

    for d in desafios:
        Display.header(d["pregunta"])
        Display.footer()
        cols    = Display.get_cols()
        padding = (cols - Display.WIDTH) // 2
        print(" " * (padding + 2), end="")
        usuario = input(FUCSIA + "  clase / objeto / salir: " + RESET).strip().lower()

        if usuario == "salir":
            Display.header("Saliendo del minijuego")
            Display.row(f"Respondiste {total_respondidas} de {len(desafios)} preguntas.", FUCSIA)
            Display.row(f"Puntos: {puntos}/{total_respondidas if total_respondidas > 0 else len(desafios)}", MORADO)
            Display.footer()
            return

        total_respondidas += 1

        if usuario == d["respuesta"]:
            Display.header("¡Correcto!")
            Display.row("Estas dominando la abstraccion.", MORADO)
            puntos += 1
        else:
            Display.header("Incorrecto")
            Display.row(f"Eso era un/a {d['respuesta'].upper()}.", MORADO)
        Display.footer()

    Display.header(f"RESULTADO FINAL: {puntos}/{len(desafios)}")
    if puntos == len(desafios):
        Display.row("Lo tienes claro. CLASE = molde, OBJETO = instancia.", MORADO)
    else:
        Display.row("Si tiene datos especificos es un OBJETO.", MORADO)
        Display.row("Si es un diseno general es una CLASE.", MORADO)
    Display.footer()