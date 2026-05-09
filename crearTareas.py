import pickle
import os
import re
from datetime import datetime

ARCHIVO = "tareas.pkl"

def guardar_tareas(tareas):
    with open(ARCHIVO, "wb") as f:
        pickle.dump(tareas, f)

def crearTarea(tareas):
    print("\n--- CREAR NUEVA TAREA ---")

    # ID
    while True:
        id_tarea = input("ID de la tarea (formato AA000): ").strip().upper()
        if not id_tarea:
            print("  ✗ El ID no puede estar vacío.")
        elif not re.fullmatch(r"[A-Z]{2}\d{3}", id_tarea):
            print("  ✗ El ID debe tener 2 letras seguidas de 3 números (ej: AB123).")
        elif id_tarea in tareas:
            print(f"  ✗ Ya existe una tarea con el ID '{id_tarea}'.")
        else:
            break

    # Título
    while True:
        titulo = input("Título: ").strip()
        if titulo:
            break
        print("  ✗ El título no puede estar vacío.")

    # Descripción
    while True:
        descripcion = input("Descripción: ").strip()
        if descripcion:
            break
        print("  ✗ La descripción no puede estar vacía.")

    # Prioridad
    while True:
        prioridad = input("Prioridad (ALTA / MEDIA / BAJA): ").strip().upper()
        if prioridad in ("ALTA", "MEDIA", "BAJA"):
            break
        print("  ✗ Ingresa una prioridad válida en mayúsculas: ALTA, MEDIA o BAJA.")

    # Fecha de vencimiento
    while True:
        fecha_str = input("Fecha de vencimiento (YYYY-MM-DD): ").strip()
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
            break
        except ValueError:
            print("  ✗ Formato inválido. Usa YYYY-MM-DD (ej: 2025-12-31).")

    tareas[id_tarea] = {
    "id": id_tarea,
    "titulo": titulo,
    "descripcion": descripcion,
    "prioridad": prioridad,
    "estado": "PENDIENTE",           # ← añadir esta línea
    "fecha_vencimiento": fecha,
}

    guardar_tareas(tareas)
    print(f"\n  ✓ Tarea '{titulo}' creada exitosamente con ID '{id_tarea}'.")