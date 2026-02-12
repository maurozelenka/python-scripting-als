# 📜 Tema 2: Listas y Tuplas

> **Asignatura:** Aplicaciones y Lenguajes de Script  

---

## 📋 Tabla de Contenidos

1. [Introducción](#-introducción)
2. [Listas](#-listas)
3. [Slicing (Rebanadas)](#-slicing-rebanadas)
4. [Operaciones con Listas](#-operaciones-con-listas)
5. [Comprensión de Listas](#-comprensión-de-listas)
6. [Tuplas](#-tuplas)
7. [Diferencias Clave](#-diferencias-clave-lista-vs-tupla)
8. [Evaluación Booleana (Truthiness)](#-evaluación-booleana-truthiness)
9. [Errores Comunes](#-errores-comunes)
10. [Conversión Lista-String](#-conversión-lista-string-join)
11. [Ordenación: sort() vs sorted()](#-ordenación-sort-vs-sorted)
12. [Funciones Integradas Útiles](#-funciones-integradas-útiles)
13. [Ejercicios Prácticos](#-ejercicios-prácticos)

---

## 🔍 Introducción

Python basa gran parte de su potencia en el manejo de secuencias.

* **Listas (`list`):** Secuencias mutables de elementos (pueden cambiar).
* **Tuplas (`tuple`):** Secuencias inmutables (son de "solo lectura").

Ambas permiten almacenar elementos heterogéneos (números, strings, otras listas, etc.).

---

## 📚 Listas

Las listas se definen con corchetes `[]`.

```python
# Lista vacía
l0 = []

# Lista con datos mixtos
lista = [11, 21, 31, 41, "texto"]

# Función len()
print(len(lista))  # Devuelve el tamaño
```

### Recorrer Listas

Existen varias formas de iterar:

```python
l = [10, 20, 30]

# 1. Bucle for-each (estándar en Python)
for x in l:
    print(f"El elemento es {x}")

# 2. Bucle con índice usando enumerate() (Recomendado si necesitas la posición)
for i, x in enumerate(l):
    print(f"Posición {i}: Valor {x}")
```

---

## ✂️ Slicing (Rebanadas)

El slicing permite obtener subconjuntos de la lista. La sintaxis es `lista[inicio:fin:paso]`.

- **inicio:** Inclusivo (por defecto 0).
- **fin:** Exclusivo (por defecto el final).
- **paso:** Salto entre elementos (por defecto 1).

```python
l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(l[0:2])      # [0, 1] (del 0 al 2 exclusive)
print(l[:])        # Copia completa de la lista
print(l[::2])      # [0, 2, 4, 6, 8] (de 2 en 2)

# Índices negativos (cuentan desde el final)
print(l[-1])       # 9 (Último elemento)
print(l[::-1])     # [9, 8, ... 0] (Invierte la lista)
print(l[-1:1:-1])  # Desde el último hasta el índice 1 (hacia atrás)
```

**Nota:** Modificar un slice modifica la lista original si se hace asignación directa, pero obtener un slice devuelve una nueva lista.

---

## 🛠️ Operaciones con Listas

| Operador/Método | Descripción | Ejemplo |
|-----------------|-------------|---------|
| `l.append(x)` | Añade x al final. | `l.append(5)` |
| `+` | Concatena listas. | `l1 + l2` |
| `*` | Repite la lista. | `['a'] * 3 -> ['a', 'a', 'a']` |
| `in / not in` | Comprueba existencia. | `5 in l -> True` |
| `del l[i]` | Borra elemento en posición i. | `del l[0]` |

---

## ⚡ Comprensión de Listas

Es una forma sintáctica ("sugar syntax") para crear listas a partir de otras, aplicando filtros o transformaciones en una sola línea.

**Sintaxis:** `[expresion for variable in iterable if condicion]`

```python
datos = [1, 2, 3, 4, 5]

# Transformación (Map): Multiplicar por 2
dobles = [x * 2 for x in datos]
# Resultado: [2, 4, 6, 8, 10]

# Filtrado (Filter): Solo los menores de 4
filtrados = [x for x in datos if x < 4]
# Resultado: [1, 2, 3]

# Combinado
complejo = [x * 2 for x in datos if x % 2 == 0]
```

---

## 🔒 Tuplas

Las tuplas son secuencias inmutables. Se definen con paréntesis `()`, aunque lo que realmente define la tupla es la coma `,`.

```python
t1 = ()          # Tupla vacía
t2 = (1, 2, 3)   # Tupla normal
t3 = (1,)        # Tupla de UN elemento (ojo a la coma)
no_es_tupla = (1)  # Esto es un entero, no una tupla
```

### Usos comunes

- **Proteger datos:** Asegurar que no se modifiquen.
- **Claves de diccionario:** Las tuplas pueden ser claves (las listas no).
- **Retorno múltiple y Desempaquetado:**

```python
# Desempaquetado (Unpacking)
punto = (10, 20)
x, y = punto  # x=10, y=20

# Intercambio de variables (Swapping)
a = 5
b = 10
a, b = b, a  # Python hace el swap internamente usando tuplas
```

---

## 🔍 Evaluación Booleana (Truthiness)

En Python, las listas pueden evaluarse en contextos booleanos (como en un `if`).

**Regla:**
- Lista **vacía** `[]` → `False`
- Lista **con elementos** → `True`

```python
bool([])           # False
bool([1, 2, 3])    # True

# Uso práctico en condicionales
lista = []
if lista:
    print("La lista tiene elementos")
else:
    print("La lista está vacía")  # Se ejecuta esto
```

---

## ⚠️ Errores Comunes

### IndexError: Acceso a índices inexistentes

Intentar acceder a una posición que no existe provoca un error **fatal** (`IndexError`).

```python
L0 = []
# L0[0]  # ❌ IndexError: list index out of range

# Forma segura de verificar antes de acceder
if len(L0) > 0:
    print(L0[0])
else:
    print("Lista vacía")
```

### Errores de Sintaxis en Bucles

**❌ INCORRECTO (esto NO es Python):**
```python
# for i in range(5)
#     print(i)
# next i  # ← Esto no existe en Python
```

**✅ CORRECTO:**
```python
for i in range(5):
    print(i)
# No se necesita cierre explícito, solo indentación
```

### Rangos Inversos

**⚠️ CUIDADO:** El segundo parámetro en `range()` es **exclusivo**.

```python
l = [0, 1, 2, 3, 4]

# ❌ INCORRECTO: Se detiene en índice 1, no llega al 0
for i in range(len(l), 0, -1):
    print(i)  # Imprime: 5, 4, 3, 2, 1

# ✅ CORRECTO: Llega hasta el índice 0
for i in range(len(l) - 1, -1, -1):
    print(l[i])  # Imprime todos los elementos en orden inverso
```

---

## 🔗 Conversión Lista-String (join)

El método `join()` une los elementos de una lista en un **único string**.

**⚠️ IMPORTANTE:** Todos los elementos deben ser **strings**.

```python
# ✅ CORRECTO: Lista de strings
palabras = ["Hola", "mundo", "Python"]
resultado = " ".join(palabras)
print(resultado)  # "Hola mundo Python"

# ❌ INCORRECTO: Lista con números
numeros = [1, 2, 3, 4, 5]
# ",".join(numeros)  # ❌ TypeError: sequence item 0: expected str instance, int found

# ✅ SOLUCIÓN: Convertir a strings primero
resultado = ",".join([str(x) for x in numeros])
print(resultado)  # "1,2,3,4,5"

# Otra forma usando map()
resultado = ",".join(map(str, numeros))
print(resultado)  # "1,2,3,4,5"
```

---

## 🔄 Ordenación: sort() vs sorted()

Existen **dos formas** de ordenar listas en Python, con comportamientos diferentes.

| Característica | `lista.sort()` | `sorted(lista)` |
|----------------|----------------|-----------------|
| **Tipo** | Método de lista | Función built-in |
| **Modifica original** | ✅ SÍ (in-place) | ❌ NO |
| **Devuelve** | `None` | Nueva lista ordenada |
| **Uso** | Cuando no necesitas la original | Cuando quieres conservar la original |

```python
original = [3, 1, 4, 1, 5]

# 1. sort() - Modifica la lista original
original.sort()
print(original)  # [1, 1, 3, 4, 5]

# 2. sorted() - Crea una nueva lista
original = [3, 1, 4, 1, 5]
ordenada = sorted(original)
print(ordenada)   # [1, 1, 3, 4, 5]
print(original)   # [3, 1, 4, 1, 5] (sin cambios)

# Ordenación inversa
original.sort(reverse=True)  # Descendente in-place
descendente = sorted(original, reverse=True)  # Descendente nueva lista
```

---

## 🧰 Funciones Integradas Útiles

Python ofrece funciones built-in muy útiles para trabajar con listas.

### sum() - Suma de elementos

```python
numeros = [1, 2, 3, 4, 5]
total = sum(numeros)
print(total)  # 15

# Con valor inicial
total = sum(numeros, 10)  # Suma + 10
print(total)  # 25
```

### max() y min() - Máximo y mínimo

```python
numeros = [3, 1, 4, 1, 5, 9, 2]
print(max(numeros))  # 9
print(min(numeros))  # 1
```

### reverse() - Invertir lista (in-place)

**⚠️ DIFERENCIA IMPORTANTE:**

```python
lista = [1, 2, 3, 4, 5]

# 1. reverse() - Modifica la original, devuelve None
lista.reverse()
print(lista)  # [5, 4, 3, 2, 1]

# 2. Slicing [::-1] - Crea una copia invertida
lista = [1, 2, 3, 4, 5]
invertida = lista[::-1]
print(invertida)  # [5, 4, 3, 2, 1]
print(lista)      # [1, 2, 3, 4, 5] (sin cambios)
```

### len() - Longitud

```python
lista = [1, 2, 3]
print(len(lista))  # 3
```

### any() y all() - Evaluación booleana

```python
numeros = [0, 1, 2, 3]
print(any(numeros))  # True (al menos un elemento es True)
print(all(numeros))  # False (no todos son True, el 0 es False)

positivos = [1, 2, 3]
print(all(positivos))  # True (todos son True)
```

---

## 🆚 Diferencias Clave: Lista vs Tupla

| Característica | Listas `[]` | Tuplas `()` |
|----------------|-------------|-------------|
| **Mutabilidad** | Mutables (se pueden editar) | Inmutables (fijas) |
| **Velocidad** | Ligeramente más lentas | Más rápidas y ligeras |
| **Usos** | Colecciones de datos dinámicos | Datos fijos, coordenadas, configuración |
| **Sintaxis** | `[1, 2]` | `(1, 2)` |

```python
# Conversión entre tipos
l = [1, 2]
t = tuple(l)  # De lista a tupla
l2 = list(t)  # De tupla a lista
```

---

## 💻 Ejercicios Prácticos

### Ejercicio 1: Calcular Media de Números

**Enunciado:** Escribe un programa que acepte varios enteros por teclado y visualice su media. Hasta que se introduzca un cero.

```python
def calcular_media():
    numeros = []
    while True:
        numero = introducir_numeros()
        if numero == 0:
            break
        numeros.append(numero)
    
    if len(numeros) == 0:
        print("No se introdujeron números.")
    else:
        media = sum(numeros) / len(numeros)
        print(f"La media de los números introducidos es: {media}")

def introducir_numeros():
    numero = int(input("Introduce un número entero (0 para terminar): "))
    return numero

# Ejecutar
calcular_media()
```

**Conceptos aplicados:**
- Lista dinámica con `append()`
- Bucle `while` con condición de salida
- Función `sum()` para sumar elementos
- Validación con `len()` antes de calcular

---

### Ejercicio 2: Mostrar Dígitos de un Número

**Enunciado:** Escribe un programa que muestre los dígitos de un número en base 10 introducido por teclado.

```python
def mostrar_digitos():
    numero = int(input("Introduce un número entero en base 10: "))
    
    # Dividiendo entre 10 y obteniendo el resto
    digitos = []
    while numero > 0:
        digito = numero % 10      # Obtener último dígito
        digitos.append(digito)     # Añadir a la lista
        numero = numero // 10      # Eliminar último dígito
    
    digitos.reverse()  # Para mostrar los dígitos en el orden correcto
    
    print("Los dígitos del número son:")
    for digito in digitos:
        print(digito)

# Ejecutar
mostrar_digitos()
```

**Conceptos aplicados:**
- Operador módulo `%` para extraer dígitos
- División entera `//`
- Método `reverse()` para invertir lista in-place
- Bucle `while` con condición numérica

**Ejemplo de ejecución:**
```
Introduce un número entero en base 10: 12345
Los dígitos del número son:
1
2
3
4
5
```