import pickle
import os

ARCHIVO = "tareas.pkl"

ESTADOS_VALIDOS = ("PENDIENTE", "EN_PROGRESO", "COMPLETADA")


def guardar_tareas(tareas):
    with open(ARCHIVO, "wb") as f:
        pickle.dump(tareas, f)


def actualizarEstadoTarea(tareas):
    print("\n--- ACTUALIZAR ESTADO DE TAREA ---")
    id_tarea = input("Ingresa el ID de la tarea: ").strip().upper()

    if not id_tarea:
        print("  ✗ Debes ingresar un ID.")
        return

    if id_tarea not in tareas:
        print(f"  ✗ No se encontró ninguna tarea con el ID '{id_tarea}'.")
        return

    print(f"  Estado actual: {tareas[id_tarea].get('estado', 'PENDIENTE')}")
    print("  Estados disponibles: PENDIENTE / EN_PROGRESO / COMPLETADA")

    nuevo_estado = input("Nuevo estado: ").strip().upper()

    if nuevo_estado not in ESTADOS_VALIDOS:
        print(f"  ✗ Estado inválido. Usa: PENDIENTE, EN_PROGRESO o COMPLETADA.")
        return

    tareas[id_tarea]["estado"] = nuevo_estado
    guardar_tareas(tareas)
    print(f"\n  ✓ Estado de la tarea '{id_tarea}' actualizado a '{nuevo_estado}'.")
