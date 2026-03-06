# Eres el gerente de un supermercado. Tienes una lista de artículos junto con sus precios
# que los clientes compraron en un día determinado. Tu tarea es imprimir cada item_name
# y net_price en el orden de su primera aparición.
# item_name = Nombre del artículo. net_price = Cantidad vendida multiplicada por el precio de cada artículo.
# La primera línea contiene el número de artículos N. Las siguientes N líneas contienen
# el nombre del artículo y su precio, separados por un espacio.
# Imprime el item_name y net_price en orden de su primera aparición.

from collections import OrderedDict

pedidos = OrderedDict()

n = int(input())
for _ in range(n):
    linea = input().split()
    precio = int(linea[-1])
    nombre = " ".join(linea[:-1])
    pedidos[nombre] = pedidos.get(nombre, 0) + precio

for nombre, total in pedidos.items():
    print(nombre, total)
