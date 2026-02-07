# Ejercicio 6: Calculadora simple

def pedir_datos():
    """Pide dos números y un operador.
    
    :return: Tupla con (num1, num2, operador).
    """
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    operador = input("Introduce el operador (+, -, *, /, ^): ")
    return num1, num2, operador

def calcular(num1, num2, operador):
    """Realiza la operación indicada.
    
    :param num1: Primer número.
    :param num2: Segundo número.
    :param operador: Operador (+, -, *, /, ^).
    :return: Resultado de la operación.
    """
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        return num1 / num2
    elif operador == '^':
        return num1 ** num2
    else:
        return "Operador no válido"

# Código principal
num1, num2, operador = pedir_datos()
resultado = calcular(num1, num2, operador)
print(f"Resultado: {resultado}")
