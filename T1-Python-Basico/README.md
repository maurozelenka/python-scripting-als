# 🐍 Tema 1: Introducción a Python

> **Asignatura:** Aplicaciones y Lenguajes de Script  

---

## 📋 Tabla de Contenidos

1. [Comentarios](#-comentarios)
2. [Entrada y Salida de Datos](#-entrada-y-salida-de-datos)
3. [Tipos de Datos](#-tipos-de-datos)
4. [Condicionales](#-condicionales)
5. [Indentación y Estructuras de Control](#-indentación-y-estructuras-de-control)
6. [Bucles (Loops)](#-bucles-loops)
7. [Funciones](#-funciones)
8. [Paso de Parámetros](#-paso-de-parámetros)
9. [Devolución Múltiple y Funciones Anidadas](#-devolución-múltiple-y-funciones-anidadas)
10. [Documentación de Funciones](#-documentación-de-funciones)
11. [Python 2 vs Python 3](#-python-2-vs-python-3)
12. [Entornos de Desarrollo](#-entornos-de-desarrollo)
13. [Virtual Environment (venv)](#-virtual-environment-venv)
14. [Linter](#-linter)
15. [Resumen de Conceptos Clave](#-resumen-de-conceptos-clave)
16. [Buenas Prácticas](#-buenas-prácticas)

---

## 💬 Comentarios

Los comentarios en Python comienzan con `#` y se descartan durante la ejecución.

```python
# Esto es un comentario de una línea
x = 5  # Comentario al final de una línea

# Los comentarios ayudan a explicar el código
# y son ignorados por el intérprete
```

**Nota:** Python **NO usa punto y coma (`;`)** para terminar líneas. El salto de línea indica el fin de la sentencia.

---

## 📥 Entrada y Salida de Datos

### Entrada de Datos

La función `input()` permite solicitar información al usuario. **Importante:** siempre devuelve una cadena de caracteres.

```python
# Solicitar entrada del usuario
x = input("Introduzca un número: ")  # input() siempre devuelve una cadena

# Conversión a número real
num = float(x)  # Convierte x en un número real (flotante)

# Conversión a número entero
num = int(x)  # Convierte x en un número entero
```

### Salida de Datos

La función `print()` muestra información en la consola y puede recibir múltiples argumentos.

```python
# Salida simple
print("Hola Mundo!!")

# Múltiples argumentos separados por comas
print("El número es", x)

# Formato avanzado con format()
print("El número es: {0:.2f} y su doble {1:.2f}".format(x, x*2))
```

**Explicación del formato:**
- Cada `{}` encierra los argumentos de formato
- El **primer argumento** (opcional) es el índice de la variable en `format()`
- El **segundo argumento** indica la representación (ej: `.2f` = 2 decimales)

---

## 🔢 Tipos de Datos

### Números

Python soporta números **enteros** (`int`) y **reales** (`float`).

**Operaciones disponibles:**
- Asignación y comparación: `=`, `==`
- Aritméticas: `+`, `-`, `*`, `/`, `%` (módulo), `**` (potencia)
- Compuestas: `+=`, `-=`, `*=`, etc.

```python
# Incremento y decremento
i = 5
i += 1  # i ahora vale 6 (equivalente a i = i + 1)
```

**Conversiones de tipo:**
```python
str(42)      # Convierte número a cadena: "42"
float("3.14")  # Convierte cadena a número real: 3.14
int("10")      # Convierte cadena a entero: 10
```

### Cadenas (Strings)

Python soporta **tipado dinámico**: una variable puede cambiar de tipo durante la ejecución.

```python
# Cadenas multilínea con triple comilla
str1 = """Esto es una 
prueba"""  # Equivalente a utilizar \n

# Funciones útiles para cadenas
len(str1)           # Devuelve el tamaño de la cadena
print(str1[0])      # Las cadenas son iterables, acceso por índice
print(str1.lower()) # Convierte a minúsculas
print(str1.upper()) # Convierte a mayúsculas
print(str1.capitalize())  # Primera letra en mayúscula
```

**Nota:** Aunque Python tiene tipado dinámico, existen formas de "tipar" estáticamente las variables (type hints).

### Operadores de Cadenas

```python
# Concatenación con +
word = 'Help' + 'A'  # 'HelpA'

# Repetición con *
word = 'Hola' * 3  # 'HolaHolaHola'

# Combinación
word = '<' + 'Help' * 2 + '>'  # '<HelpHelp>'
```

**Importante:** Los operadores `+` y `*` NO modifican las cadenas originales, sino que crean nuevas cadenas.

### Acceso a Caracteres (Slicing Básico)

```python
palabra = "Python"
print(palabra[0])     # 'P' (primer carácter)
print(palabra[0:2])   # 'Py' (del 0 al 2, sin incluir el 2)
print(palabra[2:4])   # 'th' (del 2 al 4, sin incluir el 4)
print(palabra[-1])    # 'n' (último carácter)
```

- Los índices comienzan en **0**
- Los índices negativos cuentan desde el final (-1 es el último)
- El formato es `[inicio:fin]` donde `fin` es **exclusivo**

---

## 🔀 Condicionales

### if, elif, else

```python
x = 10

if x == 5:
    print("El número es 5")
elif x > 5:
    print("El número es mayor que 5")
else:
    print("El número es menor que 5")
```

### Condicional Ternario

```python
print("Es 10" if x == 10 else "No es 10")
```

### Operadores Booleanos

Python utiliza operadores booleanos diferentes de Java o C:

- `and` → Y lógico (AND)
- `or` → O lógico (OR)
- `not` → Negación (NOT)
- `is` → Igualdad de objetos (identidad)

```python
if x > 5 and x < 15:
    print("x está entre 5 y 15")

if not x == 0:
    print("x no es cero")
```

---

## 📏 Indentación y Estructuras de Control

### Python es un Lenguaje de Indentación

Python **NO usa llaves `{}`** como Java o C. En su lugar, usa **indentación obligatoria** (espacios o tabulaciones) para definir bloques de código.

```python
if x > 5:
    print("Dentro del if")    # 4 espacios = dentro
    print("También dentro")   # mismo nivel = mismo bloque
print("Fuera del if")         # 0 espacios = fuera
```

**Convención:** Se recomienda usar **4 espacios** por nivel de indentación (PEP 8).

### Estructuras que NO Existen

- **`switch/case`**: No existe nativamente (hasta Python 3.10 existe `match-case`). Alternativa: usar `if-elif-else` o diccionarios.
- **`do-while`**: No existe. Alternativa: `while True:` con `break`.

```python
# Alternativa a do-while
while True:
    codigo
    if not condicion:
        break
```

### Problemas de Indentación

**IMPORTANTE:** Python es **muy estricto** con la indentación.

❌ **Errores comunes:**
```python
# Mezclar espacios y tabulaciones (IndentationError)
if x > 5:
    print("4 espacios")
	print("1 tab")  # ERROR!

# Indentación inconsistente
if x > 5:
    print("4 espacios")
      print("6 espacios")  # ERROR!
```

**Reglas:**
- **Python 3:** Solo acepta **espacios** (no tabuladores reales)
- **Python 2:** Acepta espacios o tabs, pero NO mezclados
- Configurar el editor para convertir TAB → 4 espacios
- Usar siempre el mismo método de indentación en todo el archivo

---

## 🔁 Bucles (Loops)

### Bucle `while`

```python
i = 0
while i < 10:
    print(i + 1)
    i += 1
```

### Bucle `for`

```python
# range() devuelve una secuencia de números (objeto iterable)
for i in range(10):  # Del 0 al 9
    print(i + 1)

# range con inicio, fin e incremento
for i in range(0, 10, 2):  # 0, 2, 4, 6, 8 (incremento de 2)
    print(i + 1)

# Iterar sobre una lista (similar a foreach)
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    print(number + 1)
```

**Parámetros de `range()`:**
- `range(fin)` → De 0 a fin-1
- `range(inicio, fin)` → De inicio a fin-1
- `range(inicio, fin, paso)` → De inicio a fin-1 con incremento de 'paso'

### Cláusula `else` en Bucles

Tanto `while` como `for` pueden tener una cláusula `else` que se ejecuta cuando el bucle termina normalmente (sin `break`).

```python
# else con while
n = 0
while n < 3:
    print(n)
    n += 1
else:
    print("Bucle while terminado")

# else con for
for i in range(3):
    print(i)
else:
    print("Bucle for terminado")
```

---

## ⚙️ Funciones

### Sintaxis Básica

```python
def name(arg1, arg2, arg3):
    # código
    return valor  # return es opcional
```

### Ejemplo: Función Recursiva

```python
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
```

### Type Hints (Python 3+)

Python3 permite especificar tipos de datos para mayor claridad:

```python
def sum(a: int, b: int) -> int:
    return a + b
```

- `a: int, b: int` → Los parámetros deben ser enteros
- `-> int` → La función devuelve un entero

### Valor de Retorno por Defecto

**Las funciones SIEMPRE devuelven un valor**, incluso sin `return` explícito. Ese valor es `None` (equivalente a `null` o `NULL` en otros lenguajes).

```python
def saludar(nombre):
    print(f"Hola, {nombre}")
    # No hay return

resultado = saludar("Ana")  # Imprime "Hola, Ana"
print(resultado)             # None
```

---

## 📦 Paso de Parámetros

### Regla General

- **Valores inmutables** (str, número, tupla) → Se pasan **por valor**
- **Valores mutables** (lista, objeto, diccionario) → Se pasan **por referencia**

```python
x = 5
l = [1, 2]

def inc(n):
    n += 1

inc(x)  # x no cambia (pasado por valor)
inc(l)  # l SÍ cambia (pasado por referencia)

print(x, l)  # Salida: 5 [1, 2, 1]
```

---

## 🔄 Devolución Múltiple y Funciones Anidadas

### Retornar Múltiples Valores

```python
def pide_datos_persona():
    def input_int(msg):  # Función anidada
        return int(input(msg))
    
    nombre = input("Dame tu nombre: ")
    apellidos = input("Dame tus apellidos: ")
    edad = input_int("Dame tu edad: ")
    
    return nombre, apellidos, edad  # Devuelve 3 valores

# Capturar los 3 valores devueltos
nombre, apellidos, edad = pide_datos_persona()
print("{1}, {0}: {2}".format(nombre, apellidos, edad))
```

**Características:**
- Las **funciones anidadas** solo son visibles dentro de la función contenedora
- Se pueden devolver múltiples valores separados por comas
- Se capturan en el mismo orden en que se devuelven

---

## 📖 Documentación de Funciones

### Docstrings

```python
def factorial(n):
    """Calcula el factorial de un número entero positivo de forma recursiva.
    
    :param n: Número entero positivo del cual se desea calcular el factorial.
    :return: El factorial de n.
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Mostrar la documentación
help(factorial)  # Similar al comando 'man' de Linux
```

**Beneficios:**
- Documenta el propósito de la función
- Describe parámetros y valores de retorno
- Accesible mediante `help(nombre_funcion)`

### Convenciones de Docstrings (PEP 257)

**Reglas básicas:**
1. Empezar con mayúscula y terminar en punto
2. Usar siempre triple comilla `"""`
3. NO repetir el nombre de la función
4. Sin líneas en blanco antes/después de la docstring
5. Parámetros: usar `:param nombre:` como prefijo
6. Retorno: usar `:return:` como prefijo

**Para documentación multilínea:**
```python
def funcion_compleja(a, b):
    """Resumen en una línea.
    
    Explicación detallada después de una línea en blanco.
    Puede extenderse varios párrafos.
    
    :param a: Descripción del parámetro a.
    :param b: Descripción del parámetro b.
    :return: Descripción de lo que devuelve.
    """
    return a + b
```

---

## 🔄 Python 2 vs Python 3

**Python 3 introdujo cambios NO compatibles con Python 2:**

| Característica | Python 2 | Python 3 |
|---------------|----------|----------|
| **print** | `print "Hola"` (operador) | `print("Hola")` (función) |
| **input** | `raw_input()` | `input()` |
| **División** | `5 / 2 = 2` (trunca) | `5 / 2 = 2.5` (real) |
| **División entera** | `5 / 2 = 2` | `5 // 2 = 2` |
| **Formato strings** | `"Hola %s" % nombre` | `"Hola {}".format(nombre)` |

**Ejemplo Python 2:**
```python
x = raw_input("Numero: ")
num = float(x)
print "El numero es %.2f" % num
```

**Equivalente Python 3:**
```python
x = input("Numero: ")
num = float(x)
print("El numero es {0:.2f}".format(num))
```

---

## 💻 Entornos de Desarrollo

### Consola Interactiva

Ejecutar `python` en la terminal abre un **REPL** (Read-Eval-Print Loop):

```bash
$ python
>>> print("Hola")
Hola
>>> 5 + 3
8
>>> quit()  # Salir
```

### IDLE

**IDLE** es el entorno gráfico oficial de Python, más cómodo que la consola de texto.

### Archivos .py

Crear y ejecutar programas:

```bash
# Crear archivo
$ echo "print('Hola')" > hola.py

# Ejecutar
$ python hola.py
Hola
```

### Compilación Automática

- Python **compila** automáticamente los archivos `.py` a **bytecode** (`.pyc`)
- La primera ejecución compila y ejecuta
- Ejecuciones posteriores solo ejecutan (si no hubo cambios)
- Acelera la carga de módulos

---

## 🌐 Virtual Environment (venv)

### ¿Qué es un Virtual Environment?

Un entorno virtual aislado para instalar dependencias de Python sin afectar el sistema global.

### Instalación (Linux)

```bash
# Actualizar repositorios
sudo apt update

# Instalar el paquete python3-venv
sudo apt install python3-venv

# Crear un entorno virtual llamado .venv
python3 -m venv .venv
```

### Activación

**En Linux:**
```bash
source .venv/bin/activate
```

**En Windows:**
```powershell
.venv\Scripts\Activate.ps1
```

### Uso

```bash
# Activar entorno
source .venv/bin/activate

# (venv) aparecerá en el prompt
(venv) $ pip install paquete

# Desactivar entorno
(venv) $ deactivate
```

---

## 🔍 Linter

### ¿Qué es un Linter?

Herramienta de análisis de código estático que detecta:
- Problemas de estilo
- Errores potenciales
- Code smells (código problemático)

### Pylint

Herramienta de análisis específica para Python que verifica:
- Cumplimiento de estándares (PEP 8)
- Errores de sintaxis y lógica
- Calidad del código

### Instalación y Uso

```bash
# Activar el entorno virtual
source .venv/bin/activate

# Instalar pylint
(venv) $ pip install pylint

# Ejecutar el linter
(venv) $ pylint archivo.py
# Devuelve una puntuación del 0 al 10

# Salir del entorno virtual
(venv) $ deactivate
```

### Interpretación de Resultados

Pylint asigna una puntuación de **0 a 10** según:
- Convenciones de código
- Errores detectados
- Warnings y refactorizaciones sugeridas

---

## 📚 Resumen de Conceptos Clave

| Concepto | Descripción |
|----------|-------------|
| `#` | Comentarios (línea completa o al final de línea) |
| `input()` | Siempre devuelve string, requiere conversión |
| `print()` | Acepta múltiples argumentos, soporta format() |
| Tipado dinámico | Las variables pueden cambiar de tipo |
| `+` en strings | Concatenación de cadenas |
| `*` en strings | Repetición de cadenas |
| Slicing `[0:2]` | Acceso a subsecuencias (caracteres de cadena) |
| `and`, `or`, `not` | Operadores booleanos de Python |
| `range()` | Genera secuencias numéricas iterables |
| `else` en bucles | Se ejecuta si el bucle termina sin `break` |
| Type hints | Anotaciones de tipo opcionales (Python 3+) |
| `None` | Valor por defecto que devuelven las funciones |
| Paso por valor | Inmutables: str, int, float, tuple |
| Paso por referencia | Mutables: list, dict, objetos |
| Docstrings | Documentación en triple comilla (`"""`) |
| PEP 257 | Convenciones para escribir docstrings |
| Indentación | 4 espacios, NO mezclar con tabs |
| Python 2 vs 3 | `print`, `input`, división, formato |
| IDLE | Entorno gráfico oficial de Python |
| `.pyc` | Bytecode compilado automáticamente |
| venv | Entornos virtuales aislados |
| Pylint | Linter para verificar calidad del código |

---

## 🎯 Buenas Prácticas

1. **Usa type hints** para mayor claridad en funciones
2. **Documenta tus funciones** con docstrings
3. **Trabaja en entornos virtuales** para aislar dependencias
4. **Ejecuta pylint** regularmente para mantener calidad de código
5. **Sigue PEP 8** (guía de estilo de Python)
6. **Nombra variables descriptivamente** en lugar de `x`, `y`, `z`
7. **Evita código duplicado** mediante funciones reutilizables

---

*Universidade de Vigo - Aplicaciones y Lenguajes de Script*
