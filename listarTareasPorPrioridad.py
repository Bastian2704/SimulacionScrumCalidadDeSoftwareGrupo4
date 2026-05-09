def listarTareasPorPrioridad(tareas):
    print("\n--- LISTAR TAREAS POR PRIORIDAD ---")

    if not tareas:
        print("  ✗ No hay tareas registradas.")
        return

    grupos = {"ALTA": [], "MEDIA": [], "BAJA": []}

    for tarea in tareas.values():
        prioridad = tarea.get("prioridad", "").upper()
        if prioridad in grupos:
            grupos[prioridad].append(tarea)

    for nivel in ("ALTA", "MEDIA", "BAJA"):
        print(f"\n  ══ Prioridad {nivel} ({len(grupos[nivel])} tarea(s)) ══")
        if not grupos[nivel]:
            print("    (Sin tareas en este nivel)")
        else:
            for tarea in grupos[nivel]:
                print("  ┌─────────────────────────────────")
                print(f"  │ ID             : {tarea['id']}")
                print(f"  │ Título         : {tarea['titulo']}")
                print(f"  │ Descripción    : {tarea['descripcion']}")
                print(f"  │ Estado         : {tarea.get('estado', 'PENDIENTE')}")
                print(f"  │ Vencimiento    : {tarea['fecha_vencimiento'].strftime('%Y-%m-%d')}")
                print("  └─────────────────────────────────")
