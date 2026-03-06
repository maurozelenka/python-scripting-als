# Crea un programa que permita guardar y hacer búsquedas sobre pares de (nombre, e.mail). El programa presentará un menú
# principal, con las opciones introducir, borrar y buscar. Al introducir datos, se pide un nombre y un e.mail, y se guardan.
# Para borrar, sólo se pide el nombre, se busca y se borra. Para buscar, sólo se pide el nombre, se busca y se muestra.
# Se debe utilizar un diccionario para guardar los datos. Créese una función que pida un nombre y devuelva el valor asociado
# (el método get() devuelve None si no se encuentra la clave), como soporte para las otras tres.
# ¿Puedes crear fácilmente una opción más, listado, que liste todas las entradas (nombre, email)?

agenda = {}


def buscar_nombre(nombre: str):
    return agenda.get(nombre)


def introducir():
    nombre = input("Nombre: ").strip()
    email = input("E-mail: ").strip()
    agenda[nombre] = email
    print(f"  '{nombre}' guardado correctamente.")


def borrar():
    nombre = input("Nombre a borrar: ").strip()
    if buscar_nombre(nombre) is not None:
        del agenda[nombre]
        print(f"  '{nombre}' eliminado.")
    else:
        print(f"  '{nombre}' no encontrado.")


def buscar():
    nombre = input("Nombre a buscar: ").strip()
    email = buscar_nombre(nombre)
    if email is not None:
        print(f"  {nombre} -> {email}")
    else:
        print(f"  '{nombre}' no encontrado.")


def listado():
    if not agenda:
        print("  La agenda está vacía.")
    else:
        print(f"  {'Nombre':<25} {'E-mail'}")
        print("  " + "-" * 50)
        for nombre, email in sorted(agenda.items()):
            print(f"  {nombre:<25} {email}")


def menu():
    opciones = {
        "1": ("Introducir", introducir),
        "2": ("Borrar",     borrar),
        "3": ("Buscar",     buscar),
        "4": ("Listado",    listado),
        "5": ("Salir",      None),
    }

    while True:
        print("\n=== AGENDA ===")
        for clave, (nombre, _) in opciones.items():
            print(f"  {clave}. {nombre}")
        opcion = input("Opción: ").strip()

        if opcion == "5":
            print("Hasta luego.")
            break
        elif opcion in opciones:
            _, funcion = opciones[opcion]
            funcion()
        else:
            print("  Opción no válida.")


menu()
