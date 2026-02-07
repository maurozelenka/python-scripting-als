# Ejercicio 7: Formateador de números de teléfono

def letra_a_digito(letra):
    """Convierte una letra a su dígito correspondiente.
    
    :param letra: Letra a convertir (a-z).
    :return: Dígito como string.
    """
    letra = letra.lower()
    if letra in 'abc':
        return '2'
    elif letra in 'def':
        return '3'
    elif letra in 'ghi':
        return '4'
    elif letra in 'jkl':
        return '5'
    elif letra in 'mno':
        return '6'
    elif letra in 'pqrs':
        return '7'
    elif letra in 'tuv':
        return '8'
    elif letra in 'wxyz':
        return '9'
    else:
        return ''

def formatear_telefono(telefono):
    """Formatea un número de teléfono.
    
    :param telefono: Número de teléfono sin formatear.
    :return: Número de teléfono formateado.
    """
    # Extraer solo dígitos y convertir letras
    digitos = ""
    for char in telefono:
        if char.isdigit():
            digitos += char
        elif char.isalpha():
            digitos += letra_a_digito(char)
    
    # Detectar código de país
    codigo_pais = ""
    numero = digitos
    
    if telefono.startswith('+') and len(digitos) >= 2:
        codigo_pais = '+' + digitos[:2]
        numero = digitos[2:]
    elif telefono.startswith('00') and len(digitos) >= 4:
        codigo_pais = '+' + digitos[2:4]
        numero = digitos[4:]
    
    # Formatear número en grupos de 3
    numero_formateado = ""
    for i, digito in enumerate(numero):
        if i > 0 and i % 3 == 0:
            numero_formateado += " "
        numero_formateado += digito
    
    # Resultado final
    if codigo_pais:
        return f"{codigo_pais} {numero_formateado}"
    else:
        return numero_formateado

# Código principal
telefono = input("Introduce el número de teléfono: ")
resultado = formatear_telefono(telefono)
print(f"Número formateado: {resultado}")
