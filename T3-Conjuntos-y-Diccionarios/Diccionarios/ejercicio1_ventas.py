# Supón las siguientes líneas de datos. La primera especifica los nombres de las empresas, y las siguientes la empresa,
# la fecha del lunes de esa semana, y las ventas para cada día de la semana. Crea una función que lea esa información
# como una cadena de texto separada por cambios de línea, y genere un informe que sea sencillo de entender por el ser humano.

DIAS_SEMANA = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


def generar_informe(datos: str) -> str:
    lineas = [l.strip() for l in datos.strip().splitlines() if l.strip()]

    partes_empresas = [p.strip() for p in lineas[0].split(",")]
    empresas = {}
    for i in range(0, len(partes_empresas), 2):
        nombre = partes_empresas[i]
        empresa_id = partes_empresas[i + 1]
        empresas[empresa_id] = nombre

    registros = []
    for linea in lineas[1:]:
        partes = [p.strip() for p in linea.split(",")]
        empresa_id = partes[0]
        fecha = partes[1]
        ventas = list(map(int, partes[2:9]))
        registros.append((empresa_id, fecha, ventas))

    informe = []
    informe.append("=" * 52)
    informe.append("         INFORME DE VENTAS SEMANALES")
    informe.append("=" * 52)

    semanas = sorted(set(r[1] for r in registros))

    for semana in semanas:
        informe.append(f"\nSemana del {semana}")
        informe.append("-" * 52)

        registros_semana = [r for r in registros if r[1] == semana]

        for empresa_id, fecha, ventas in registros_semana:
            nombre = empresas.get(empresa_id, f"Empresa {empresa_id}")
            total = sum(ventas)
            promedio = total / len(ventas)
            maximo = max(ventas)
            dia_max = DIAS_SEMANA[ventas.index(maximo)]

            informe.append(f"\n  {nombre}")
            for i, dia in enumerate(DIAS_SEMANA):
                informe.append(f"    {dia:<12}: {ventas[i]:>6}")
            informe.append(f"    {'─' * 22}")
            informe.append(f"    {'Total':<12}: {total:>6}")
            informe.append(f"    {'Promedio/día':<12}: {promedio:>6.1f}")
            informe.append(f"    {'Mejor día':<12}: {dia_max} ({maximo})")

    informe.append("\n" + "=" * 52)
    return "\n".join(informe)


datos_ejemplo = """Microsoft, 1, Apple, 2, Google, 3, Yahoo, 4
1, 2015-01-09, 120, 34, 256, 78, 93, 222, 5
2, 2015-01-09, 900, 346, 730, 456, 33, 345, 234
3, 2015-01-09, 934, 922, 866, 444, 235, 999, 789
4, 2015-01-09, 45, 56, 78, 23, 44, 90, 9"""

print(generar_informe(datos_ejemplo))
