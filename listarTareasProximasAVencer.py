from datetime import date


def listarTareasProximasAVencer(tareas, dias=7):
    print(f"\n--- TAREAS PRÓXIMAS A VENCER (próximos {dias} días) ---")

    if not tareas:
        print("  ✗ No hay tareas registradas.")
        return

    hoy = date.today()
    proximas = []

    for tarea in tareas.values():
        fecha_venc = tarea.get("fecha_vencimiento")
        if fecha_venc is None:
            continue
        diferencia = (fecha_venc - hoy).days
        if 0 <= diferencia <= dias:
            proximas.append((diferencia, tarea))

    proximas.sort(key=lambda x: x[0])

    if not proximas:
        print(f"  ✗ No hay tareas que venzan en los próximos {dias} días.")
        return

    print(f"\n  Se encontraron {len(proximas)} tarea(s) próximas a vencer:\n")
    for dias_restantes, tarea in proximas:
        print("  ┌─────────────────────────────────")
        print(f"  │ ID             : {tarea['id']}")
        print(f"  │ Título         : {tarea['titulo']}")
        print(f"  │ Prioridad      : {tarea['prioridad']}")
        print(f"  │ Estado         : {tarea.get('estado', 'PENDIENTE')}")
        print(f"  │ Vencimiento    : {tarea['fecha_vencimiento'].strftime('%Y-%m-%d')}")
        print(f"  │ Días restantes : {dias_restantes}")
        print("  └─────────────────────────────────")
