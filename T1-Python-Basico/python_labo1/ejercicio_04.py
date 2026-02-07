# Ejercicio 4: Área y perímetro de circunferencia

def calcular_area(radio):
    """Calcula el área de una circunferencia.
    
    :param radio: El radio de la circunferencia.
    :return: El área.
    """
    return 3.1416 * radio ** 2

def calcular_perimetro(radio):
    """Calcula el perímetro de una circunferencia.
    
    :param radio: El radio de la circunferencia.
    :return: El perímetro.
    """
    return 2 * 3.1416 * radio

# Código principal
radio = float(input("Introduce el radio de la circunferencia: "))
area = calcular_area(radio)
perimetro = calcular_perimetro(radio)

print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")
