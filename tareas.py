import pickle
import os
import re
from datetime import datetime
from crearTareas import crearTarea
from buscarTareaPorId import buscarTareaPorId, cargar_tareas

# ARCHIVO = "tareas.pkl"


# def cargar_tareas():
#     if os.path.exists(ARCHIVO):
#         with open(ARCHIVO, "rb") as f:
#             return pickle.load(f)
#     return {}


# def guardar_tareas(tareas):
#     with open(ARCHIVO, "wb") as f:
#         pickle.dump(tareas, f)


# def crearTarea(tareas):
#     print("\n--- CREAR NUEVA TAREA ---")

#     # ID
#     while True:
#         id_tarea = input("ID de la tarea (formato AA000): ").strip().upper()
#         if not id_tarea:
#             print("  ✗ El ID no puede estar vacío.")
#         elif not re.fullmatch(r"[A-Z]{2}\d{3}", id_tarea):
#             print("  ✗ El ID debe tener 2 letras seguidas de 3 números (ej: AB123).")
#         elif id_tarea in tareas:
#             print(f"  ✗ Ya existe una tarea con el ID '{id_tarea}'.")
#         else:
#             break

#     # Título
#     while True:
#         titulo = input("Título: ").strip()
#         if titulo:
#             break
#         print("  ✗ El título no puede estar vacío.")

#     # Descripción
#     while True:
#         descripcion = input("Descripción: ").strip()
#         if descripcion:
#             break
#         print("  ✗ La descripción no puede estar vacía.")

#     # Prioridad
#     while True:
#         prioridad = input("Prioridad (ALTA / MEDIA / BAJA): ").strip().upper()
#         if prioridad in ("ALTA", "MEDIA", "BAJA"):
#             break
#         print("  ✗ Ingresa una prioridad válida en mayúsculas: ALTA, MEDIA o BAJA.")

#     # Fecha de vencimiento
#     while True:
#         fecha_str = input("Fecha de vencimiento (YYYY-MM-DD): ").strip()
#         try:
#             fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
#             break
#         except ValueError:
#             print("  ✗ Formato inválido. Usa YYYY-MM-DD (ej: 2025-12-31).")

#     tareas[id_tarea] = {
#         "id": id_tarea,
#         "titulo": titulo,
#         "descripcion": descripcion,
#         "prioridad": prioridad,
#         "fecha_vencimiento": fecha,
#     }

#     guardar_tareas(tareas)
#     print(f"\n  ✓ Tarea '{titulo}' creada exitosamente con ID '{id_tarea}'.")


# def buscarTareaPorId(tareas):
#     print("\n--- BUSCAR TAREA POR ID ---")
#     termino = input("Ingresa el ID o parte del ID: ").strip().upper()

#     if not termino:
#         print("  ✗ Debes ingresar un ID.")
#         return

#     coincidencias = [t for clave, t in tareas.items() if termino in clave]

#     if not coincidencias:
#         print(f"  ✗ No se encontró ninguna tarea que coincida con '{termino}'.")
#         return

#     print(f"\n  Se encontraron {len(coincidencias)} resultado(s):\n")
#     for tarea in coincidencias:
#         print("  ┌─────────────────────────────────")
#         print(f"  │ ID             : {tarea['id']}")
#         print(f"  │ Título         : {tarea['titulo']}")
#         print(f"  │ Descripción    : {tarea['descripcion']}")
#         print(f"  │ Prioridad      : {tarea['prioridad']}")
#         print(f"  │ Vencimiento    : {tarea['fecha_vencimiento'].strftime('%Y-%m-%d')}")
#         print("  └─────────────────────────────────")


def mostrar_menu():
    print("\n=============================")
    print("     GESTOR DE TAREAS")
    print("=============================")
    print("  1. Crear tarea")
    print("  2. Buscar tarea por ID")
    print("  3. Salir")
    print("=============================")


def main():
    tareas = cargar_tareas()
    print("Bienvenido al Gestor de Tareas.")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción (1-3): ").strip()

        if opcion == "1":
            crearTarea(tareas)
        elif opcion == "2":
            buscarTareaPorId(tareas)
        elif opcion == "3":
            print("\nHasta luego. 👋")
            break
        else:
            print("  ✗ Opción inválida. Elige 1, 2 o 3.")


if __name__ == "__main__":
    main()