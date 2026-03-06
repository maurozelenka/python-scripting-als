# Se dan dos grupos de palabras A y B de tamaños n y m respectivamente. Las palabras del grupo A
# pueden repetirse. Para cada palabra del grupo B, se deben imprimir los índices (basados en 1)
# de cada aparición de esa palabra en el grupo A. Si no aparece, imprimir -1.
# La primera línea contiene n y m separados por espacio. Las siguientes n líneas son las palabras
# del grupo A. Las siguientes m líneas son las palabras del grupo B.

from collections import defaultdict

n, m = map(int, input().split())

grupo_a = defaultdict(list)
for i in range(1, n + 1):
    palabra = input()
    grupo_a[palabra].append(i)

for _ in range(m):
    palabra = input()
    print(*grupo_a[palabra] if grupo_a[palabra] else [-1])
