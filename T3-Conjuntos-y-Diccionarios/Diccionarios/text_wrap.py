# Se da una cadena de texto y un ancho máximo. La tarea es envolver la cadena en un párrafo
# de ese ancho, dividiendo la cadena en líneas de longitud máxima max_width.
# La primera línea contiene la cadena. La segunda línea contiene el ancho máximo.

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

string = input()
max_width = int(input())
print(wrap(string, max_width))
