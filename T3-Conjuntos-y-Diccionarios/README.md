# 📜 Tema 3: Diccionarios y Conjuntos

> **Asignatura:** Aplicaciones y Lenguajes de Script  

---

## 📋 Tabla de Contenidos

1. [Introducción](#-introducción)
2. [Conjuntos (Sets)](#-conjuntos-sets)
3. [Operaciones con Conjuntos](#-operaciones-con-conjuntos)
4. [Diccionarios (Dictionaries)](#-diccionarios-dictionaries)
5. [Operaciones con Diccionarios](#-operaciones-con-diccionarios)
6. [Recorrer Diccionarios](#-recorrer-diccionarios)
7. [Patrones Comunes](#-patrones-comunes)
8. [Simulando switch con Diccionarios](#-simulando-switch-con-diccionarios)
9. [Generadores vs Listas](#-generadores-vs-listas)
10. [Ejercicios Prácticos](#-ejercicios-prácticos)

---

## 🔍 Introducción

Python proporciona dos estructuras de datos fundamentales adicionales:

* **Conjuntos (`set`):** Colecciones **no ordenadas** de elementos **únicos** (sin duplicados).
* **Diccionarios (`dict`):** Colecciones de pares **clave-valor**, donde cada clave es única.

Ambas estructuras son **mutables** (se pueden modificar después de crearlas) y permiten elementos heterogéneos.

---

## 🎯 Conjuntos (Sets)

Los conjuntos son secuencias **sin orden** y **sin elementos repetidos**. Ideales para eliminar duplicados y realizar operaciones matemáticas de conjuntos.

### Creación de Conjuntos

**⚠️ IMPORTANTE:** No se puede usar `{}` para crear un conjunto vacío (crea un diccionario vacío).

```python
# ❌ INCORRECTO: Crea un diccionario vacío
c0 = {}
type(c0)  # <class 'dict'>

# ✅ CORRECTO: Conjunto vacío
c0 = set()
type(c0)  # <class 'set'>

# Conjunto con elementos
c1 = {1, 2, 3, 4, 5}

# Crear conjunto desde lista (elimina duplicados automáticamente)
l = [1, 2, 2, 3, 3, 4, 4, 5]
c = set(l)
print(c)  # {1, 2, 3, 4, 5}
```

### Características Fundamentales

1. **Sin duplicados:** Automáticamente elimina elementos repetidos
2. **No indexables:** No se puede acceder por índice como `c[0]`
3. **No ordenados:** El orden no está garantizado
4. **Elementos hashables:** Solo pueden contener elementos inmutables (números, strings, tuplas)

```python
# ❌ ERROR: Listas no son hashables
c = {[1, 2, 3]}  # TypeError: unhashable type: 'list'

# ✅ CORRECTO: Tuplas sí son hashables
c = {(1, 2, 3), (4, 5, 6)}
```

### Operaciones Básicas

```python
c = {11, 22, 33, 44, 55, 66}

# Comprobar pertenencia
5 in c       # False
11 in c      # True
10 not in c  # True

# Añadir elemento
c.add(77)
print(c)  # {11, 22, 33, 44, 55, 66, 77}

# Eliminar elemento
c.remove(22)  # Si no existe, lanza KeyError
c.discard(22) # Si no existe, NO lanza error (más seguro)

# Tamaño del conjunto
len(c)  # 6

# Limpiar conjunto
c.clear()
```

### Recorrer Conjuntos

**Método 1: Directamente (for-each)**
```python
c = {11, 22, 33, 44, 55, 66}

for x in c:
    print(x, end=" ")  # 11 22 33 44 55 66 (orden no garantizado)
```

**Método 2: Convertir a lista (para indexar)**
```python
# Acceder por índice (convirtiendo a lista)
print(list(c)[2:])  # Obtiene desde el índice 2 en adelante

# Recorrer con índice
for i, x in enumerate(list(c)):
    print(f"Posición {i}: {x}")
```

### Eliminar Duplicados de una Lista

**Patrón muy común:**

```python
# Lista con duplicados
l = [1, 1, 1, 2, 2, 2, 2, 3, 3]

# Convertir a conjunto (elimina duplicados) y luego a lista
l = list(set(l))
print(l)  # [1, 2, 3]
```

---

## 🔧 Operaciones con Conjuntos

Los conjuntos soportan operaciones matemáticas de teoría de conjuntos.

### Tabla de Operadores

Dados `s1 = {1, 2, 3}` y `s2 = {3, 4, 5}`:

| Operador | Operación | Resultado | Descripción |
|----------|-----------|-----------|-------------|
| `s1 \| s2` | Unión | `{1, 2, 3, 4, 5}` | Elementos en s1 **o** s2 |
| `s1 & s2` | Intersección | `{3}` | Elementos en s1 **y** s2 |
| `s1 - s2` | Diferencia | `{1, 2}` | Elementos en s1 pero **no** en s2 |
| `s1 ^ s2` | Diferencia simétrica | `{1, 2, 4, 5}` | Elementos en s1 **o** s2, pero **no** en ambos |

### Ejemplos Prácticos

```python
s1 = {1, 2, 3}
s2 = {3, 4, 5}

# Unión (todos los elementos)
print(s1 | s2)  # {1, 2, 3, 4, 5}

# Intersección (elementos comunes)
print(s1 & s2)  # {3}

# Diferencia (en s1 pero no en s2)
print(s1 - s2)  # {1, 2}

# Diferencia simétrica (no repetidos en ambos)
print(s1 ^ s2)  # {1, 2, 4, 5}

# Funciones integradas
print(min(s2))  # 3
print(max(s2))  # 5
```

### Uso Práctico: Concatenar Listas sin Repetir

```python
def concatena_listas_no_repetidos(l1, l2):
    """Concatena dos listas descartando elementos repetidos.
    
    :param l1: Primera lista
    :param l2: Segunda lista
    :return: Conjunto con elementos únicos
    """
    return set(l1) | set(l2)

l1 = [1, 2, 3, 3]
l2 = [3, 4, 5]
resultado = concatena_listas_no_repetidos(l1, l2)
print(resultado)  # {1, 2, 3, 4, 5}
```

---

## 📖 Diccionarios (Dictionaries)

Los diccionarios almacenan pares **clave-valor**. Son como "listas asociativas" donde cada clave única mapea a un valor.

### Creación de Diccionarios

```python
# Diccionario vacío
d = {}
d = dict()

# Diccionario con datos
d = {"a": 1, "b": 2, "c": 3, "d": 4}

# Diferentes tipos de claves y valores
persona = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Vigo",
    "activo": True
}
```

### Acceso a Elementos

```python
color_ojos = {
    "marron": 90,
    "gris": 3,
    "azul": 10,
    "verde": 2,
    "ambar": 5
}

# Método 1: Acceso directo con [] (lanza KeyError si no existe)
print(color_ojos["marron"])  # 90
# print(color_ojos["rojo"])  # ❌ KeyError: 'rojo'

# Método 2: Método get() (devuelve None o valor por defecto)
print(color_ojos.get("marron"))  # 90
print(color_ojos.get("rojo"))    # None
print(color_ojos.get("rojo", 0)) # 0 (valor por defecto)
```

**💡 Recomendación:** Usa `get()` cuando no estés seguro de que la clave existe.

### Modificar y Añadir Elementos

```python
temperaturas = {"Ourense": 5, "Vigo": 12}

# Modificar valor existente
temperaturas["Ourense"] += 1
print(temperaturas["Ourense"])  # 6

# Añadir nuevo par clave-valor
temperaturas["Pontevedra"] = 10
print(temperaturas)  # {'Ourense': 6, 'Vigo': 12, 'Pontevedra': 10}

# Eliminar elemento
del temperaturas["Vigo"]
print(temperaturas)  # {'Ourense': 6, 'Pontevedra': 10}
```

### Verificar Existencia

```python
d = {"a": 1, "b": 2, "c": 3}

# Verificar si una clave existe
if "a" in d:
    print("La clave 'a' existe")

if "z" not in d:
    print("La clave 'z' NO existe")

# Uso práctico con get()
color = input("Introduce un color: ").strip().lower()
porcentaje = color_ojos.get(color)

if porcentaje:
    print(f"El porcentaje de personas con ojos {color}: {porcentaje}%")
else:
    print("Ese color no está en el diccionario")
```

---

## 🔄 Operaciones con Diccionarios

### Tabla de Operadores y Métodos

Dado `d1 = {1: 'a', 2: 'b', 3: 'c'}` y `d2 = {4: 'd', 5: 'e', 6: 'f'}`:

| Operador/Método | Descripción | Resultado |
|-----------------|-------------|-----------|
| `d1[9] = 'i'` | Añade/modifica par (9, 'i') | `d1 == {1: 'a', 2: 'b', 3: 'c', 9: 'i'}` |
| `d1[9]` | Devuelve valor de clave 9 | `'i'` (KeyError si no existe) |
| `d1.get(9)` | Devuelve valor o None | `'i'` (None si no existe) |
| `d1.get(9, 'x')` | Devuelve valor o default | `'i'` ('x' si no existe) |
| `9 in d1` | Verifica si clave existe | `True` |
| `9 not in d1` | Verifica si clave no existe | `False` |
| `del d1[1]` | Elimina clave 1 y su valor | `{2: 'b', 3: 'c', 9: 'i'}` |
| `d2.clear()` | Borra todos los elementos | `d2 == {}` |
| `len(d1)` | Número de pares | `3` |
| `min(d1)` | Clave más pequeña | `2` |
| `max(d1)` | Clave más grande | `9` |
| `d1 == d2` | Compara diccionarios | `False` |

---

## 🔁 Recorrer Diccionarios

Existen tres métodos principales para iterar sobre diccionarios.

### Método 1: keys() - Solo Claves

```python
temperaturas = {"Ourense": 5, "Vigo": 12}

for k in temperaturas.keys():
    print(f"{k}: {temperaturas[k]}º")

# Salida:
# Ourense: 5º
# Vigo: 12º
```

**Nota:** `for k in temperaturas:` es equivalente a `for k in temperaturas.keys()`.

### Método 2: items() - Pares Clave-Valor (⭐ Recomendado)

```python
temperaturas = {"Ourense": 5, "Vigo": 12}

for k, v in temperaturas.items():
    print(f"{k}: {v}º")

# Salida:
# Ourense: 5º
# Vigo: 12º
```

**💡 Ventaja:** Más eficiente, no requiere buscar el valor con `temperaturas[k]`.

### Método 3: values() - Solo Valores

```python
temperaturas = {"Ourense": 5, "Vigo": 12}

for v in temperaturas.values():
    print(f"{v}º")

# Salida:
# 5º
# 12º
```

### Ejemplo Completo: Sistema de Colores de Ojos

```python
color_ojos = {
    "marron": 90,
    "gris": 3,
    "azul": 10,
    "verde": 2,
    "ambar": 5,
    "amarillo": 0,
    "rojo": 0
}

color = input("Introduce un color de ojos: ").strip().lower()
porcentaje = color_ojos.get(color)

if porcentaje:
    print(f"El porcentaje de personas con ojos {color}: {porcentaje}%")
    
    # Mostrar otros colores (excluyendo el introducido)
    print("\nOtros colores:")
    for k, v in color_ojos.items():
        if k != color:
            print(f"  {k}: {v}%")
else:
    print("Los colores disponibles son:")
    for k, v in color_ojos.items():
        print(f"  {k}: {v}%")
```

### Comprensión de Diccionarios con items()

```python
# Filtrar elementos con list comprehension
color_ojos = {"marron": 90, "azul": 10, "verde": 2}
color = "azul"

# Obtener todos los colores excepto uno
otros_colores = [(k, v) for k, v in color_ojos.items() if k != color]
print(otros_colores)  # [('marron', 90), ('verde', 2)]

# Crear nuevo diccionario con filtro
colores_raros = {k: v for k, v in color_ojos.items() if v < 5}
print(colores_raros)  # {'verde': 2}
```

---

## 🎨 Patrones Comunes

### Patrón 1: Contar Frecuencias

```python
def contar_letras(texto):
    """Cuenta la frecuencia de cada letra en un texto.
    
    :param texto: Cadena de texto a analizar
    :return: Diccionario con letra: frecuencia
    """
    d = {}
    for letra in texto:
        if letra.isalpha():  # Solo letras
            letra = letra.lower()
            d[letra] = d.get(letra, 0) + 1  # Incrementar contador
    return d

texto = "hola mundo"
print(contar_letras(texto))
# {'h': 1, 'o': 2, 'l': 1, 'a': 1, 'm': 1, 'u': 1, 'n': 1, 'd': 1}
```

### Patrón 2: Calcular Porcentajes

```python
def porcentaje_letras(texto):
    """Calcula el porcentaje de aparición de cada letra.
    
    :param texto: Cadena de texto a analizar
    :return: Diccionario con letra: porcentaje
    """
    # Contar apariciones
    d = {}
    for letra in texto:
        if letra.isalpha():
            letra = letra.lower()
            d[letra] = d.get(letra, 0) + 1
    
    # Calcular total
    total_letras = sum(d.values())
    
    # Calcular porcentajes
    porcentajes = {
        letra: (count / total_letras * 100) if total_letras > 0 else 0
        for letra, count in d.items()
    }
    
    return porcentajes

print(porcentaje_letras("hola"))
# {'h': 25.0, 'o': 25.0, 'l': 25.0, 'a': 25.0}
```

### Patrón 3: Mapeo de Reemplazos (HTML a Markdown)

```python
def html_a_markdown(html):
    """Convierte etiquetas HTML básicas a Markdown.
    
    :param html: Cadena con HTML
    :return: Cadena convertida a Markdown
    """
    # Diccionario de conversiones
    conversiones = {
        "<b>": "**",
        "</b>": "**",
        "<h1>": "# ",
        "</h1>": "\n",
        "<i>": "_",
        "</i>": "_",
        "<p>": "\n\n",
        "<li>": "- "
    }
    
    # Aplicar todas las conversiones
    for etiqueta_html, markdown in conversiones.items():
        html = html.replace(etiqueta_html, markdown)
    
    return html

html = "<h1>Título</h1><p>Esto es <b>negrita</b> y esto <i>cursiva</i>"
print(html_a_markdown(html))
# # Título
# 
# Esto es **negrita** y esto _cursiva_
```

---

## 🔀 Simulando switch con Diccionarios

Python no tiene estructura `switch`, pero se puede simular con diccionarios.

### Ejemplo Básico

```python
def funcion1():
    print("Opción 1 seleccionada")

def funcion2():
    print("Opción 2 seleccionada")

def funcion3():
    print("Opción 3 seleccionada")

# Diccionario de funciones
opciones = {
    1: funcion1,
    2: funcion2,
    3: funcion3
}

# Solicitar opción
i = int(input("Introduzca opción (1-3): "))

# Validar entrada
while i not in opciones:
    i = int(input("Introduzca opción (1-3): "))

# Ejecutar función correspondiente
opciones[i]()  # Llamada a la función
```

### Ejemplo con Parámetros

```python
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b if b != 0 else "Error: división por cero"

# Calculadora simple
operaciones = {
    "+": sumar,
    "-": restar,
    "*": multiplicar,
    "/": dividir
}

a = 10
b = 5
op = "+"

resultado = operaciones[op](a, b)  # sumar(10, 5)
print(f"{a} {op} {b} = {resultado}")  # 10 + 5 = 15
```

### Ejemplo con Valor por Defecto

```python
def opcion_default():
    print("Opción no válida")

opciones = {
    1: funcion1,
    2: funcion2,
    3: funcion3
}

opcion = int(input("Selecciona opción: "))

# Usar get() con función por defecto
funcion = opciones.get(opcion, opcion_default)
funcion()
```

---

## ⚡ Generadores vs Listas

### ¿Qué son los Generadores?

Los **generadores** son iterables que generan valores **sobre la marcha** (lazy evaluation), sin almacenar toda la secuencia en memoria.

**Sintaxis:**
- **Lista:** `[expresión for x in iterable]` (corchetes)
- **Generador:** `(expresión for x in iterable)` (paréntesis)

### Diferencias Fundamentales

```python
# Lista: Se crea completa en memoria
lista = [x * 2 for x in range(1000000)]
# Consume ~8 MB de memoria

# Generador: Solo almacena la "receta"
generador = (x * 2 for x in range(1000000))
# Consume ~80 bytes

# Para ver el contenido de un generador
print(list(generador))  # Lo convierte a lista
```

### ⚠️ Generadores No Son Hashables

```python
# ❌ ERROR: Generadores no pueden ser elementos de conjuntos
print({(x * 2 for x in [1, 2, 3])})  # TypeError

# ❌ ERROR: Listas tampoco son hashables
print({[x * 2 for x in [1, 2, 3]]})  # TypeError

# ✅ CORRECTO: Convertir a lista primero
print(list((x * 2 for x in [1, 2, 3])))  # [2, 4, 6]
```

### range() es un Generador

```python
# range() devuelve un objeto iterable, no una lista
print(range(100))  # range(0, 100)

# Para ver los valores, convertir a lista
print(list(range(100)))  # [0, 1, 2, ..., 99]
```

### Uso Eficiente en Bucles

```python
# ✅ Sintácticamente equivalente, pero generador más eficiente
for x in (x * 2 for x in range(300)):
    print(x)

# También funciona (menos eficiente en memoria)
for x in [x * 2 for x in range(300)]:
    print(x)
```

**💡 Ventaja de generadores:**
- **Memoria:** No almacenan todos los valores
- **Velocidad:** Empiezan a producir valores inmediatamente
- **Ideal para:** Secuencias grandes o infinitas

**Cuándo usar listas:**
- Necesitas acceso por índice
- Vas a iterar múltiples veces
- El tamaño es pequeño

---

## 💻 Ejercicios Prácticos

### Ejercicio 1: Puntos Cartesianos con Tuplas

**Enunciado:** Crea funciones para manejar puntos cartesianos usando tuplas, calcular el origen y la distancia entre puntos.

```python
import math

def get_origen():
    """Devuelve el origen de coordenadas.
    
    :return: Tupla (0, 0)
    """
    return (0, 0)

def get_distancia(p1, p2):
    """Calcula la distancia entre dos puntos.
    
    :param p1: Punto como tupla (x, y)
    :param p2: Punto como tupla (x, y)
    :return: Distancia como número real
    """
    a = abs(p1[0] - p2[0])
    b = abs(p1[1] - p2[1])
    return math.sqrt(a ** 2 + b ** 2)

# Uso
origen = get_origen()
print(get_distancia((2, 2), (4, 4)))  # 2.8284271247461903
print(get_distancia((2, 2), origen))   # 2.8284271247461903
```

---

### Ejercicio 2: Frecuencia de Palabras (Word Count)

**Enunciado:** Función que calcule la frecuencia de aparición de palabras en un texto.

```python
def wc(s):
    """Calcula la frecuencia de cada palabra en una cadena.
    
    :param s: Cadena de texto
    :return: Diccionario con palabra: frecuencia
    """
    palabras = s.strip().lower().split()
    frecuencias = {}
    
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
    
    return frecuencias

# Uso
texto = "Esto es una prueba esto es solo una prueba"
print(wc(texto))
# {'esto': 2, 'es': 2, 'una': 2, 'prueba': 2, 'solo': 1}
```

---

### Ejercicio 3: Detectar Anagramas

**Enunciado:** Determinar si dos cadenas son anagramas (mismas letras, distinto orden).

```python
def es_anagrama(s1, s2):
    """Comprueba si dos cadenas son anagramas.
    
    :param s1: Primera cadena
    :param s2: Segunda cadena
    :return: True si son anagramas, False en caso contrario
    """
    def cuenta_letras(s):
        """Cuenta frecuencia de cada letra."""
        conteo = {}
        for letra in s:
            conteo[letra] = conteo.get(letra, 0) + 1
        return conteo
    
    # Normalizar cadenas
    s1 = s1.strip().lower()
    s2 = s2.strip().lower()
    
    # Deben tener la misma longitud
    if len(s1) != len(s2):
        return False
    
    # Comparar conteos de letras
    return cuenta_letras(s1) == cuenta_letras(s2)

# Uso
print(es_anagrama("amor", "roma"))     # True
print(es_anagrama("python", "typhon")) # True
print(es_anagrama("hola", "adios"))    # False
```

---

### Ejercicio 4: Listas Enlazadas con Conjuntos

**Enunciado:** Implementar nodos enlazados y detectar ciclos usando conjuntos.

```python
def nuevo_nodo(valor):
    """Crea un nuevo nodo.
    
    :param valor: Valor del nodo
    :return: Lista [valor, enlace] donde enlace es None inicialmente
    """
    return [valor, None]

def enlaza_nodos(n1, n2):
    """Enlaza el nodo n1 con n2.
    
    :param n1: Nodo origen
    :param n2: Nodo destino
    """
    n1[1] = n2

def recorre_nodos(n):
    """Recorre los nodos y devuelve sus valores.
    
    :param n: Nodo inicial
    :return: Lista con valores de los nodos
    """
    valores = []
    while n is not None:
        valores.append(n[0])
        n = n[1]
    return valores

def detecta_ciclo(n):
    """Detecta si hay un ciclo en la lista enlazada.
    
    :param n: Nodo inicial
    :return: True si hay ciclo, False en caso contrario
    """
    visitados = set()
    while n:
        # Si ya visitamos este nodo, hay ciclo
        if id(n) in visitados:
            return True
        visitados.add(id(n))
        n = n[1]
    return False

# Crear lista enlazada: a -> b -> c
n1 = nuevo_nodo('a')
n2 = nuevo_nodo('b')
n3 = nuevo_nodo('c')
enlaza_nodos(n1, n2)
enlaza_nodos(n2, n3)

print(recorre_nodos(n1))     # ['a', 'b', 'c']
print(detecta_ciclo(n1))     # False

# Crear ciclo: c -> b (ahora hay ciclo)
enlaza_nodos(n3, n2)
print(detecta_ciclo(n1))     # True
```

---

### Ejercicio 5: Puntos 3D

**Enunciado:** Crear funciones para manejar puntos tridimensionales (x, y, z).

```python
import math

def getOrigen():
    """Devuelve el origen en 3D.
    
    :return: Tupla (0, 0, 0)
    """
    return (0, 0, 0)

def creaPunto(x, y, z):
    """Crea un punto 3D.
    
    :param x: Coordenada x
    :param y: Coordenada y
    :param z: Coordenada z
    :return: Tupla (x, y, z)
    """
    return (x, y, z)

def calculaDistancia(p1, p2):
    """Calcula la distancia entre dos puntos 3D.
    
    Fórmula: sqrt((x2-x1)² + (y2-y1)² + (z2-z1)²)
    
    :param p1: Primer punto (x, y, z)
    :param p2: Segundo punto (x, y, z)
    :return: Distancia como número real
    """
    dx = abs(p1[0] - p2[0])
    dy = abs(p1[1] - p2[1])
    dz = abs(p1[2] - p2[2])
    
    return math.sqrt(dx ** 2 + dy ** 2 + dz ** 2)

# Uso
origen = getOrigen()
p1 = creaPunto(1, 2, 3)
p2 = creaPunto(4, 5, 6)

print(calculaDistancia(p1, p2))      # 5.196152422706632
print(calculaDistancia(p1, origen))  # 3.7416573867739413
```

---

### Ejercicio 6: Mismas Letras (Conjuntos)

**Enunciado:** Verificar si dos palabras contienen las mismas letras (sin importar repeticiones).

```python
def mismas_letras(s1, s2):
    """Verifica si dos palabras tienen las mismas letras.
    
    :param s1: Primera palabra
    :param s2: Segunda palabra
    :return: True si tienen las mismas letras, False en caso contrario
    """
    # Convertir a conjuntos de letras (elimina duplicados)
    return set(s1.lower()) == set(s2.lower())

# Uso
print(mismas_letras("amor", "roma"))      # True
print(mismas_letras("casa", "saca"))      # True
print(mismas_letras("python", "java"))    # False
print(mismas_letras("aabbcc", "abc"))     # True (ignora repeticiones)
```

---

## 📊 Resumen Comparativo

### Listas vs Tuplas vs Conjuntos vs Diccionarios

| Característica | Lista `[]` | Tupla `()` | Conjunto `{}` | Diccionario `{}` |
|----------------|------------|------------|---------------|------------------|
| **Mutable** | ✅ Sí | ❌ No | ✅ Sí | ✅ Sí |
| **Ordenado** | ✅ Sí | ✅ Sí | ❌ No | ❌ No (Python <3.7) |
| **Indexable** | ✅ Sí | ✅ Sí | ❌ No | ✅ Por clave |
| **Duplicados** | ✅ Permite | ✅ Permite | ❌ No permite | Claves únicas |
| **Sintaxis** | `[1, 2]` | `(1, 2)` | `{1, 2}` | `{'a': 1}` |
| **Vacío** | `[]` | `()` | `set()` | `{}` |
| **Uso típico** | Secuencias | Datos fijos | Sin duplicados | Mapeo clave-valor |

---

## 🎯 Consejos Finales

### Cuándo Usar Cada Estructura

**Listas:**
- Secuencias ordenadas que pueden cambiar
- Necesitas acceso por índice
- Permites duplicados

**Tuplas:**
- Datos que no deben cambiar (coordenadas, fechas)
- Retorno múltiple de funciones
- Claves de diccionarios

**Conjuntos:**
- Eliminar duplicados
- Operaciones matemáticas de conjuntos
- Búsqueda rápida de pertenencia

**Diccionarios:**
- Mapear claves a valores
- Búsquedas rápidas por clave
- Contadores y frecuencias
- Configuraciones y mapeos

### Patrones de Eficiencia

```python
# ✅ EFICIENTE: Usar get() con valor por defecto
contador = {}
contador[palabra] = contador.get(palabra, 0) + 1

# ❌ INEFICIENTE: Verificar existencia cada vez
if palabra in contador:
    contador[palabra] += 1
else:
    contador[palabra] = 1

# ✅ EFICIENTE: items() para recorrer diccionarios
for k, v in diccionario.items():
    print(k, v)

# ❌ INEFICIENTE: keys() con búsqueda
for k in diccionario.keys():
    print(k, diccionario[k])
```