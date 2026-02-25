"""
Moovi's Labo2 - Ejercicio #3
-----------------------------
Evalúa expresiones numéricas en notación PREFIJA y POSTFIJA.

Notación PREFIJA (el operador va primero):
    Ejemplo simple:    + 1 2          → 3
    Ejemplo complejo:  + 1 - 5 * 2 4 → 1 + (5 - (2 * 4)) = -2

Notación POSTFIJA (el operador va al final):
    Ejemplo simple:    1 2 +          → 3
    Ejemplo complejo:  1 3 4 + +      → 1 + (3 + 4) = 8

El programa detecta automáticamente el tipo de notación:
    - Si el primer token es un operador → PREFIJA
    - Si el último token es un operador → POSTFIJA
"""

OPERATORS = {'+', '-', '*', '/'}


def apply(op, a, b):
    """Aplica el operador a dos operandos."""
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b


# ──────────────────────────────────────────────
# NOTACIÓN PREFIJA
# ──────────────────────────────────────────────

def eval_prefix(tokens, index=0):
    """
    Evalúa una expresión prefija recursivamente.
    Devuelve (resultado, siguiente_índice).
    """
    token = tokens[index]

    if token in OPERATORS:
        left, index = eval_prefix(tokens, index + 1)
        right, index = eval_prefix(tokens, index)
        return apply(token, left, right), index
    else:
        return float(token), index + 1


# ──────────────────────────────────────────────
# NOTACIÓN POSTFIJA
# ──────────────────────────────────────────────

def eval_postfix(tokens, index=None):
    """
    Evalúa una expresión postfija recursivamente (de derecha a izquierda).
    Devuelve (resultado, índice_anterior).
    """
    if index is None:
        index = len(tokens) - 1

    token = tokens[index]

    if token in OPERATORS:
        right, index = eval_postfix(tokens, index - 1)
        left, index = eval_postfix(tokens, index)
        return apply(token, left, right), index
    else:
        return float(token), index - 1


# ──────────────────────────────────────────────
# DETECCIÓN AUTOMÁTICA Y EVALUACIÓN
# ──────────────────────────────────────────────

def detect_and_evaluate(expression):
    """Detecta si la expresión es prefija o postfija y la evalúa."""
    tokens = expression.split()

    if not tokens:
        raise ValueError("Expresión vacía.")

    if tokens[0] in OPERATORS:
        tipo = "PREFIJA"
        result, _ = eval_prefix(tokens)
    elif tokens[-1] in OPERATORS:
        tipo = "POSTFIJA"
        result, _ = eval_postfix(tokens)
    else:
        raise ValueError("No se pudo determinar si la expresión es prefija o postfija.")

    if result == int(result):
        result = int(result)

    return tipo, result


# ──────────────────────────────────────────────
# PROGRAMA PRINCIPAL
# ──────────────────────────────────────────────

if __name__ == '__main__':
    print("=" * 50)
    print("  Evaluador de expresiones PREFIJAS y POSTFIJAS")
    print("=" * 50)
    print("Operadores soportados: + - * /")
    print("Ejemplos prefijos:  '+ 1 2'  |  '+ 1 - 5 * 2 4'")
    print("Ejemplos postfijos: '1 2 +'  |  '1 3 4 + +'")
    print("Escribe 'salir' para terminar.\n")

    while True:
        expr = input("Expresión: ").strip()

        if expr.lower() == 'salir':
            print("¡Hasta luego!")
            break

        try:
            tipo, resultado = detect_and_evaluate(expr)
            print(f"  → Notación {tipo}: {resultado}\n")
        except Exception as e:
            print(f"  ✗ Error: {e}\n")
