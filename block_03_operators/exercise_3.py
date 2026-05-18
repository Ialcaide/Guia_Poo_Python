import os
from core.display import Display
from core.navigator import Navigator

FUCSIA = "\033[38;2;255;0;127m"
MORADO = "\033[38;2;148;0;211m"
RESET  = "\033[0m"

def clear():
    os.system("cls" if os.name == "nt" else "clear")

# Ejercicio 3-----------------------------------------------------
def exercise_3():
    pasos = [
        {
            "titulo": "Resolución de Expresión",
            "explicacion": [
                "Tenemos la siguiente expresión matemática compleja:",
                "x = 2 + 1 * 2 % 2 + (2**1)//2"
            ],
            "calculo": None
        },
        {
            "titulo": "Paso 1: Paréntesis y Potencias ( ** )",
            "explicacion": [
                "La regla dice: lo que está entre paréntesis",
                "y las potencias ** se resuelven de primero.",
                "",
                "Evaluamos: (2**1)",
                "Esto significa: 2 elevado a la potencia 1",
                "2 ** 1 = 2",
                "",
                "Nuestra expresión ahora se ve así:",
                "x = 2 + 1 * 2 % 2 + (2)//2"
            ],
            "calculo": f"2 ** 1 = {2 ** 1}"
        },
        {
            "titulo": "Paso 2: Multiplicación ( * )",
            "explicacion": [
                "Después de las potencias, Python busca linealmente",
                "las operaciones de multiplicación y división.",
                "",
                "Evaluamos: 1 * 2",
                "1 multiplicado por 2 = 2",
                "",
                "Nuestra expresión ahora se ve así:",
                "x = 2 + 2 % 2 + (2)//2"
            ],
            "calculo": f"1 * 2 = {1 * 2}"
        },
        {
            "titulo": "Paso 3: Módulo / Residuo ( % )",
            "explicacion": [
                "El módulo % nos devuelve el residuo entero de una división.",
                "Es equivalente a preguntar: ¿Cuánto sobra?",
                "",
                "Evaluamos: 2 % 2",
                "2 dividido entre 2 es 1, y el residuo es 0.",
                "Por lo tanto: 2 % 2 = 0",
                "",
                "Nuestra expresión ahora se ve así:",
                "x = 2 + 0 + (2)//2"
            ],
            "calculo": f"2 % 2 = {2 % 2}"
        },
        {
            "titulo": "Paso 4: División Entera ( // )",
            "explicacion": [
                "La división entera // realiza la división y trunca",
                "completamente los decimales, conservando la parte entera.",
                "",
                "Evaluamos: 2 // 2",
                "2 dividido entre 2 = 1.0 (Se descarta el .0)",
                "Resultado = 1",
                "",
                "Nuestra expresión ahora se ve así:",
                "x = 2 + 0 + 1"
            ],
            "calculo": f"2 // 2 = {2 // 2}"
        },
        {
            "titulo": "Paso 5: Sumas y Restas ( + )",
            "explicacion": [
                "Las sumas y restas tienen la menor prioridad",
                "y se evalúan estrictamente de izquierda a derecha.",
                "",
                "Evaluamos: 2 + 0 + 1",
                "2 + 0 = 2",
                "2 + 1 = 3",
                "",
                "Resultado final evaluado: x = 3"
            ],
            "calculo": f"2 + 0 + 1 = {2 + 0 + 1}"
        },
        {
            "titulo": "Resumen Final de Prioridades",
            "explicacion": [
                "Expresión: x = 2 + 1 * 2 % 2 + (2**1)//2",
                "",
                "Orden de evaluación ejecutado por Python:",
                "1. ** : 2**1       = 2",
                "2. * : 1*2        = 2",
                "3. %   : 2%2        = 0",
                "4. //  : 2//2       = 1",
                "5. +   : 2+0+1      = 3",
                "",
                f"Resultado de la variable: x = {2 + 1 * 2 % 2 + (2 ** 1) // 2}",
                "",
                "REGLA MNEMOTÉCNICA JERÁRQUICA:",
                "  ()  ->  ** ->  * / // %  ->  + -",
                "(De mayor a menor prioridad de evaluación)"
            ],
            "calculo": None
        }
    ]

    paso_actual = 1
    total_pasos = len(pasos)

    while True:
        clear()
        paso = pasos[paso_actual - 1]

        # Header dinámico mostrando el número del paso
        Display.header(f"Ejercicio 3 - Paso {paso_actual}/{total_pasos}: {paso['titulo']}")
        
        for linea in paso["explicacion"]:
            Display.row(linea, MORADO)

        if paso["calculo"]:
            Display.empty()
            Display.row(f"EVALUACIÓN REALIZADA: {paso['calculo']}", FUCSIA)

        Display.footer()

        # Delegamos la navegación interactiva completamente al Navigator del core
        opcion = Navigator.navigate(paso_actual, total_pasos, has_input=False)

        if opcion == 0:
            break
        else:
            paso_actual = opcion

