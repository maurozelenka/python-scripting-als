# Ejercicio 5: Formatear coordenadas

# Versión 1: Usando str()
def fmt_coordenadas_v1(x, y):
    """Formatea coordenadas como (x, y).
    
    :param x: Coordenada x.
    :param y: Coordenada y.
    :return: Cadena formateada.
    """
    return "(" + str(x) + ", " + str(y) + ")"

# Versión 2: Usando format()
def fmt_coordenadas_v2(x, y):
    """Formatea coordenadas como (x, y).
    
    :param x: Coordenada x.
    :param y: Coordenada y.
    :return: Cadena formateada.
    """
    return "({0}, {1})".format(x, y)

# Versión 3 (bonus): Usando f-strings
def fmt_coordenadas_v3(x, y):
    """Formatea coordenadas como (x, y).
    
    :param x: Coordenada x.
    :param y: Coordenada y.
    :return: Cadena formateada.
    """
    return f"({x}, {y})"

# Código principal
x = float(input("Introduce coordenada x: "))
y = float(input("Introduce coordenada y: "))

print("Versión 1 (str):", fmt_coordenadas_v1(x, y))
print("Versión 2 (format):", fmt_coordenadas_v2(x, y))
print("Versión 3 (f-string):", fmt_coordenadas_v3(x, y))
