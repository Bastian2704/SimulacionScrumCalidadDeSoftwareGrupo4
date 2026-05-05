import pickle
import os
import re
from datetime import datetime

ARCHIVO = "tareas.pkl"


def cargar_tareas():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "rb") as f:
            return pickle.load(f)
    return {}

def buscarTareaPorId(tareas):
    print("\n--- BUSCAR TAREA POR ID ---")
    termino = input("Ingresa el ID o parte del ID: ").strip().upper()

    if not termino:
        print("  ✗ Debes ingresar un ID.")
        return

    coincidencias = [t for clave, t in tareas.items() if termino in clave]

    if not coincidencias:
        print(f"  ✗ No se encontró ninguna tarea que coincida con '{termino}'.")
        return

    print(f"\n  Se encontraron {len(coincidencias)} resultado(s):\n")
    for tarea in coincidencias:
        print("  ┌─────────────────────────────────")
        print(f"  │ ID             : {tarea['id']}")
        print(f"  │ Título         : {tarea['titulo']}")
        print(f"  │ Descripción    : {tarea['descripcion']}")
        print(f"  │ Prioridad      : {tarea['prioridad']}")
        print(f"  │ Vencimiento    : {tarea['fecha_vencimiento'].strftime('%Y-%m-%d')}")