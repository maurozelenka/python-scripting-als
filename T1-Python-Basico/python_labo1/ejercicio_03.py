# Ejercicio 3: Dividir en funciones

def pedir_nombre():
    """Pide el nombre al usuario."""
    return input("Dime tu nombre: ")

def visualizar_nombre(nombre):
    """Visualiza el saludo con el nombre."""
    print(f"Hola, {nombre}")

# Código principal
nombre = pedir_nombre()
visualizar_nombre(nombre)
