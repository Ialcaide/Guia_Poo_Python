# Guía Práctica Experimental 1 — Programación Orientada a Objetos en Python

**Materia:** Programación Orientada a Objetos  
**Semestre:** 4to Semestre — Ingeniería en Software  
**Fecha de entrega:** 18 de mayo de 2026

---

## Descripción del proyecto

Este proyecto es la entrega de la Guía 1 de POO en Python. Contiene los ejercicios de los 18 bloques temáticos organizados en un menú interactivo en consola. Cada bloque tiene sus propios ejercicios con navegación entre ellos, y al final hay una sección de ejercicios propuestos con ayuda de IA.

El programa corre completamente en consola con un diseño visual usando caracteres ASCII extendidos, colores ANSI y posicionamiento con gotoxy.

---

## Cómo ejecutar el proyecto

### Requisitos

- Python 3.10 o superior
- colorama

### Instalación de dependencias

```bash
pip install colorama
```

### Ejecución

```bash
python main.py
```

---

## Estructura del proyecto

```
PythonProject/
├── main.py
├── README.md
│
├── menu/
│   ├── __init__.py
│   └── menu.py                  <- clase Menu con gotoxy y Frame
│
├── blocks/
│   ├── __init__.py
│   ├── block_00_intro/
│   │   ├── __init__.py
│   │   ├── exercise_1.py
│   │   ├── exercise_2.py
│   │   ├── exercise_3.py
│   │   └── menu.py
│   ├── block_01_constructor/
│   │   ├── __init__.py
│   │   ├── exercise_1.py
│   │   ├── exercise_2.py
│   │   ├── exercise_3.py
│   │   ├── exercise_4.py
│   │   └── menu.py
│   ├── block_02_variables/ ... block_17_mixins/
│   └── exercises_AI.py          <- ejercicios propuestos por IA
│
├── core/
│   ├── __init__.py
│   ├── app.py                   <- clase App, punto de entrada
│   ├── colors.py                <- clase Color
│   ├── constants.py             <- colores y clear() reutilizables
│   ├── display.py               <- clase Display con gotoxy
│   ├── navigator.py             <- clase Navigator
│   └── mixins.py                <- PromedioMixin, ValidacionMixin, ExportarMixin
│
├── data/
│   ├── ejercicio1.json
│   ├── ejercicio2.json
│   ├── ejercicio3.json
│   └── inventory.json
│
└── ai_documentation/
    └── prompts_used.md
```

---

## Clases principales

| Clase | Archivo | Para qué sirve |
|---|---|---|
| `App` | `core/app.py` | Punto de entrada, contiene el menú principal y llama a cada bloque |
| `Menu` | `menu/menu.py` | Dibuja el menú con marco ASCII, colores y gotoxy centrado |
| `Frame` | `menu/menu.py` | Dibuja el marco rectangular con caracteres ASCII extendidos |
| `Display` | `core/display.py` | Muestra los ejercicios dentro de un marco con filas y colores |
| `Navigator` | `core/navigator.py` | Navegación entre ejercicios con opciones de repetir, avanzar y retroceder |
| `PromedioMixin` | `core/mixins.py` | Mixin que calcula el promedio de una lista de notas |
| `ValidacionMixin` | `core/mixins.py` | Mixin que valida email y edad |
| `ExportarMixin` | `core/mixins.py` | Mixin que exporta datos a JSON y CSV |

---

## Bloques y ejercicios

| # | Bloque | Ejercicios |
|---|---|---|
| 00 | Intro a POO | Clases biblioteca, clase Persona, clase vs objeto |
| 01 | Constructor `__init__` | Productos, validación precio, estudiante con notas, classmethod |
| 02 | Variables y tipos | Tipos simples y complejos, listas, clase con str/list/dict |
| 03 | Operadores | Aritméticos, == vs is, precedencia de operadores |
| 04 | Input y Output | f-strings, suma y promedio, concatenación sin conversión |
| 05 | Condicionales | Par o impar, calificación por letra, sistema de login |
| 06 | Bucles | While del 1 al 10, enumerate con frutas, list comprehension |
| 07 | Funciones | Doble de un número, suma con *args, factorial recursivo |
| 08 | Listas | append y sort, sum/max/min, referencia vs copia |
| 09 | Tuplas | Tupla inmutable, unpacking, recorrer coordenadas |
| 10 | Diccionarios | Acceso con [] y get(), iterar items, referencia vs copia |
| 11 | Conjuntos | Unión/intersección/diferencia, eliminar duplicados, diferencia simétrica |
| 12 | Excepciones | ValueError, IndexError, ZeroDivisionError |
| 13 | Decoradores | Decorador log, validar positivo, @log en suma |
| 14 | Unpacking | Desempaquetar tupla, *args en función, combinar dicts con ** |
| 15 | Funciones orden superior | map(), filter(), reduce() |
| 16 | Archivos y JSON | Escribir/leer JSON, guardar dict, lista de usuarios |
| 17 | Mixins | PromedioMixin, ValidacionMixin, ExportarMixin |
| Extra | Ejercicios IA | Un ejercicio práctico por cada bloque |

---

## Implementación del gotoxy

El profesor exigió el uso de `gotoxy(x, y)` para posicionar el cursor en la consola. Lo implementé en dos lugares:

**En `menu/menu.py`** para dibujar el marco y centrar el menú:

```python
def gotoxy(x: int, y: int):
    sys.stdout.write(f"\033[{y};{x}H")
    sys.stdout.flush()
```

**En `core/display.py`** para posicionar el cursor del input:

```python
@staticmethod
def gotoxy(x: int, y: int):
    sys.stdout.write(f"\033[{y};{x}H")
    sys.stdout.flush()

@staticmethod
def input_at(prompt: str) -> str:
    cols = Display.get_cols()
    x    = (cols - Display.WIDTH) // 2 + 4
    y    = 35
    Display.gotoxy(x, y)
    return input(FUCSIA + f"  {prompt} " + RESET)
```

La clase `Frame` usa `gotoxy` para dibujar cada carácter del marco en su posición exacta, lo que permite un diseño limpio y centrado independientemente del tamaño de la terminal.

---

## Uso de Inteligencia Artificial

Para el desarrollo de esta tarea utilicé **Claude (Anthropic)** como herramienta de apoyo en el aprendizaje, siguiendo la metodología indicada por el profesor: entender el concepto, pedir un proceso similar y resolverlo por mi cuenta.

---

## Documentación de prompts por bloque

### Bloque 00 — Introducción a POO

**IA utilizada:** Claude

**Prompt para entender el ejercicio:**
"Explícame la diferencia entre una clase y un objeto en Python con un ejemplo de la vida real, como si fuera a alguien que nunca ha programado"

**Respuesta resumida de la IA:**
La IA explicó que una clase es como el plano de una casa (define cómo será) y un objeto es la casa construida (tiene valores reales). La clase `Persona` define que toda persona tiene nombre y edad, y `persona_1 = Persona("Daniel", 20)` es el objeto real con datos específicos.

**Prompt para proceso similar:**
"Dame un ejercicio similar usando un sistema de tienda en vez de biblioteca, con 5 clases relacionadas entre sí"

**Mi resolución propia:**
Creé las clases `Product`, `Customer`, `Order`, `Category` y `Supplier` con sus atributos y las instancié con datos de ejemplo.

---

### Bloque 01 — Constructor `__init__`

**IA utilizada:** Claude

**Prompt para entender el ejercicio:**
"Explícame qué es el constructor __init__ en Python, para qué sirve self, y cómo se hace un @classmethod que cree un objeto desde un diccionario"

**Respuesta resumida de la IA:**
El constructor `__init__` se ejecuta automáticamente al crear un objeto y `self` representa al objeto actual. El `@classmethod` permite crear objetos de formas alternativas, por ejemplo desde un diccionario.

**Prompt para proceso similar:**
"Dame un ejercicio similar creando una clase Vehiculo con marca, modelo y año, con validaciones y un classmethod desde_diccionario"

**Mi resolución propia:**
Implementé la clase `Vehicle` con validación de año (no menor a 1900) y el método `from_dictionary` que recibe un dict con las claves `brand`, `model` y `year`.

---

### Bloque 02 — Variables y tipos de datos

**IA utilizada:** Claude

**Prompt para entender el ejercicio:**
"Explícame todos los tipos de datos en Python: int, float, str, bool, None, list, tuple, dict y set con ejemplos de cada uno"

**Respuesta resumida de la IA:**
La IA mostró cada tipo con ejemplos y explicó que los tipos simples guardan un solo valor y los complejos guardan colecciones. También explicó el acceso por índice y el slicing.

**Prompt para proceso similar:**
"Dame un ejercicio donde declare una variable de cada tipo y acceda a elementos específicos de las colecciones"

**Mi resolución propia:**
Declaré variables de todos los tipos y accedí al primer elemento, último y un slice de la lista.

---

### Bloque 03 — Operadores

**IA utilizada:** Claude

**Prompt para entender el ejercicio:**
"Explícame la precedencia de operadores en Python paso a paso con la expresión x = 2 + 1 * 2 % 2 + (2**1)//2, como si fuera a un niño"

**Respuesta resumida de la IA:**
La IA explicó que Python evalúa primero `**`, luego `*`, `//`, `%`, y por último `+` y `-`. Mostró el proceso paso a paso: `2**1=2`, `1*2=2`, `2%2=0`, `2//2=1`, `2+0+1=3`.

**Prompt para proceso similar:**
"Dame una expresión similar con los mismos operadores pero con números diferentes para practicar el orden"

**Mi resolución propia:**
Resolví la expresión original y creé una versión interactiva que muestra cada paso del cálculo en pantalla.

---

### Bloque 04 — Input y Output

**IA utilizada:** Claude

**Prompt para entender el ejercicio:**
"¿Por qué input() siempre devuelve string en Python y qué pasa si intento sumar ese string con un número sin convertirlo?"

**Respuesta resumida de la IA:**
La IA explicó que `input()` retorna siempre `str` porque Python no sabe qué tipo de dato quiere el usuario. Si se suma `"10" + "5"` se obtiene `"105"` porque se concatenan como texto.

**Prompt para proceso similar:**
"Dame un ejercicio donde el usuario ingrese dos números, se calculen la suma y el promedio, y se muestren con f-string"

**Mi resolución propia:**
Implementé la lectura con validación de tipo `float` para aceptar decimales y mostré los resultados con f-string.

---

### Bloque 05 — Condicionales

**IA utilizada:** Claude

**Prompt para entender el ejercicio:**
"Explícame cómo hacer un sistema de login en Python que verifique usuario y contraseña por separado y diga cuál de los dos está incorrecto"

**Respuesta resumida de la IA:**
La IA explicó que se puede verificar primero el usuario y si está bien, verificar la contraseña. Si el usuario falla, solo se pide que corrija el usuario. Si la contraseña falla, solo se pide la contraseña.

**Prompt para proceso similar:**
"Dame un ejercicio de sistema de login con 3 intentos máximos y que muestre cuántos intentos quedan"

**Mi resolución propia:**
Implementé el login con contador de intentos, validación separada de usuario y contraseña, y bloqueo tras 3 intentos fallidos.

---

### Bloque 06 — Bucles

**IA utilizada:** Claude

**Prompt para entender el ejercicio:**
"Explícame la diferencia entre for y while en Python, cómo funciona enumerate() y qué es list comprehension con un filtro"

**Respuesta resumida de la IA:**
`while` repite mientras una condición sea verdadera. `for` recorre una colección. `enumerate()` da el índice y el valor al mismo tiempo. List comprehension es una forma corta de crear listas con condición incluida.

**Prompt para proceso similar:**
"Dame un ejercicio usando list comprehension para obtener los cuadrados de los números impares del 1 al 20"

**Mi resolución propia:**
Usé `[x**2 for x in range(1, 21) if x % 2 != 0]` y mostré el proceso explicando qué pasa con cada número.

---

### Bloque 07 — Funciones

**IA utilizada:** Claude

**Prompt para entender el ejercicio:**
"Explícame qué son *args en Python, cómo funciona la recursividad y por qué necesita un caso base"

**Respuesta resumida de la IA:**
`*args` permite recibir cualquier cantidad de argumentos posicionales. La recursividad es cuando una función se llama a sí misma. El caso base es la condición que detiene las llamadas recursivas, sin él el programa entraría en un bucle infinito.

**Prompt para proceso similar:**
"Dame un ejercicio de función recursiva diferente al factorial, como la suma de los primeros n números"

**Mi resolución propia:**
Implementé `sum_recursive(n)` donde el caso base es `n == 0` y la llamada recursiva es `n + sum_recursive(n-1)`.

---

### Bloque 08 — Listas

**IA utilizada:** Claude

**Prompt para entender el ejercicio:**
"Explícame la diferencia entre copia por referencia y copia real en Python con listas, y por qué es importante"

**Respuesta resumida de la IA:**
Cuando haces `b = a`, ambas variables apuntan al mismo objeto en memoria. Si modificas `b`, también modificas `a`. Para hacer una copia independiente debes usar `a.copy()`.

**Prompt para proceso similar:**
"Dame un ejercicio donde se vea claramente la diferencia usando id() para mostrar las direcciones de memoria"

**Mi resolución propia:**
Mostré los tres casos: referencia directa, copia con `.copy()` y la diferencia usando `id()` para verificar que son objetos distintos.

---

### Bloque 09 — Tuplas

**IA utilizada:** Claude

**Prompt para entender el ejercicio:**
"Explícame qué significa que las tuplas sean inmutables en Python y qué es el unpacking con el operador *"

**Respuesta resumida de la IA:**
Inmutable significa que no se puede cambiar después de crearse. Si intentas modificar un elemento lanza `TypeError`. El unpacking con `*` captura múltiples valores restantes en una lista.

**Prompt para proceso similar:**
"Dame un ejercicio de unpacking con coordenadas geográficas donde se desempaquete latitud, longitud y nombre de ciudad"

**Mi resolución propia:**
Creé una lista de tuplas con coordenadas reales de ciudades y las recorrí desempaquetando `lat`, `lon` y `city` en cada iteración.

---

### Bloque 10 — Diccionarios

**IA utilizada:** Claude

**Prompt para entender el ejercicio:**
"Explícame la diferencia entre acceder a un diccionario con [] y con get() en Python, y cuándo usar cada uno"

**Respuesta resumida de la IA:**
Con `[]` lanza `KeyError` si la clave no existe. Con `.get()` retorna `None` o un valor por defecto si no encuentra la clave. Se usa `.get()` cuando no se está seguro de que la clave existe.

**Prompt para proceso similar:**
"Dame un ejercicio donde el usuario cree un diccionario con datos personales, lo itere y demuestre la diferencia entre [] y get()"

**Mi resolución propia:**
Creé un diccionario de persona con valores fijos y mostré el acceso con ambos métodos, incluyendo un acceso a una clave inexistente con `get()`.

---

### Bloque 11 — Conjuntos

**IA utilizada:** Claude

**Prompt para entender el ejercicio:**
"Explícame las operaciones matemáticas de conjuntos en Python: unión, intersección, diferencia y diferencia simétrica con ejemplos"

**Respuesta resumida de la IA:**
La IA usó la analogía de dos grupos de estudiantes con materias. La unión (`|`) da todas las materias, la intersección (`&`) da las que comparten, la diferencia (`-`) da las exclusivas de uno, y la diferencia simétrica (`^`) da las que no comparten.

**Prompt para proceso similar:**
"Dame un ejercicio usando conjuntos para encontrar materias en común entre dos estudiantes universitarios"

**Mi resolución propia:**
Definí dos conjuntos con materias de estudiantes diferentes y calculé todas las operaciones mostrando el resultado explicado.

---

### Bloque 12 — Excepciones

**IA utilizada:** Claude

**Prompt para entender el ejercicio:**
"Explícame cómo funciona try/except en Python para manejar múltiples tipos de error en el mismo bloque"

**Respuesta resumida de la IA:**
Se pueden poner varios `except` para diferentes tipos de error. Python evalúa de arriba hacia abajo y ejecuta el primero que coincida con el error lanzado.

**Prompt para proceso similar:**
"Dame un ejercicio donde se capturen ValueError, ZeroDivisionError e IndexError en el mismo try/except"

**Mi resolución propia:**
Implementé una calculadora que captura los tres tipos de error con mensajes específicos para cada uno.

---

### Bloque 13 — Decoradores

**IA utilizada:** Claude

**Prompt para entender el ejercicio:**
"Explícame qué es un decorador en Python con un ejemplo simple, y cómo se usa *args y **kwargs en el wrapper para que sea genérico"

**Respuesta resumida de la IA:**
Un decorador es una función que envuelve a otra. El `wrapper` con `*args, **kwargs` permite que el decorador funcione con cualquier función sin importar cuántos parámetros tenga.

**Prompt para proceso similar:**
"Dame un ejercicio creando un decorador que mida el tiempo de ejecución de una función usando el módulo time"

**Mi resolución propia:**
Implementé `@timer` usando `time.time()` antes y después de ejecutar la función decorada, mostrando el tiempo en segundos.

---

### Bloque 14 — Unpacking

**IA utilizada:** Claude

**Prompt para entender el ejercicio:**
"Explícame cómo funciona el operador ** para combinar diccionarios en Python y la diferencia entre * para listas y ** para diccionarios"

**Respuesta resumida de la IA:**
`*lista` desempaqueta una lista como argumentos posicionales. `**dict` desempaqueta un diccionario como argumentos con nombre. Al combinar dos dicts con `{**d1, **d2}` se crea uno nuevo sin modificar los originales.

**Prompt para proceso similar:**
"Dame un ejercicio donde se combine información de dos diccionarios de empleados sin modificar los originales"

**Mi resolución propia:**
Creé dos diccionarios con información de empleados y los combiné con `**`, verificando que los originales no cambiaron.

---

### Bloque 15 — Funciones de orden superior

**IA utilizada:** Claude

**Prompt para entender el ejercicio:**
"Explícame map(), filter() y reduce() en Python con ejemplos simples usando lambda, y cómo se pueden combinar"

**Respuesta resumida de la IA:**
`map()` aplica una función a cada elemento. `filter()` filtra elementos según una condición. `reduce()` acumula un resultado aplicando la función de izquierda a derecha. Se pueden combinar pasando el resultado de uno como entrada del otro.

**Prompt para proceso similar:**
"Dame un ejercicio combinando los tres: filtrar números pares, elevarlos al cuadrado con map y sumarlos todos con reduce"

**Mi resolución propia:**
Apliqué `filter()` para pares, `map()` para elevar al cuadrado y `reduce()` para sumar todo, mostrando el resultado de cada paso.

---

### Bloque 16 — Archivos y JSON

**IA utilizada:** Claude

**Prompt para entender el ejercicio:**
"Explícame cómo leer y escribir archivos JSON en Python con json.dump() y json.load(), incluyendo cómo manejar listas de objetos"

**Respuesta resumida de la IA:**
`json.dump(data, f)` convierte el objeto Python a JSON y lo guarda. `json.load(f)` lee el JSON y lo convierte a objeto Python. Con `indent=2` el archivo queda legible.

**Prompt para proceso similar:**
"Dame un ejercicio que guarde una lista de productos con nombre y precio en JSON y luego los cargue y muestre"

**Mi resolución propia:**
Guardé una lista de diccionarios de productos en `data/inventory.json` y los cargué mostrando cada producto con su precio.

---

### Bloque 17 — Mixins

**IA utilizada:** Claude

**Prompt para entender el ejercicio:**
"Explícame qué es un Mixin en Python, en qué se diferencia de la herencia normal y cuándo usarlo"

**Respuesta resumida de la IA:**
Un Mixin es una clase diseñada para agregar funcionalidad específica a otras clases mediante herencia múltiple. No se usa sola. La diferencia con herencia normal es que el Mixin no representa una entidad del mundo real, solo agrega comportamiento reutilizable.

**Prompt para proceso similar:**
"Dame un ejercicio creando un LogMixin que registre todas las operaciones realizadas y se pueda agregar a cualquier clase"

**Mi resolución propia:**
Implementé `LogMixin` con un método `log_action(action)` que guarda las acciones en una lista y las puede mostrar. Lo integré en una clase `BankAccount`.

---

## Metodología de aprendizaje con IA

Seguí el ciclo indicado por el profesor en cada ejercicio:

1. Le pedí a Claude que me explicara el concepto del ejercicio con ejemplos simples
2. Le pedí un ejercicio similar para practicar
3. Resolví ese ejercicio similar por mi cuenta sin copiar la respuesta
4. Si no entendía algo, repetí el ciclo con una pregunta más específica
5. Una vez que entendí, implementé el ejercicio original de la guía

El objetivo no fue copiar código sino entender la lógica para poder aplicarla.

---

## Autor

Ileana De la Caridad Alcaide Lopez — 4to Semestre  
Materia: Programación Orientada a Objetos