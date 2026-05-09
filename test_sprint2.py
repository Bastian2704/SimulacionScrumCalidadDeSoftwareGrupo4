import unittest
from unittest.mock import patch
from io import StringIO
from datetime import date, timedelta
from actualizarEstadoTarea import actualizarEstadoTarea
from listarTareasPorPrioridad import listarTareasPorPrioridad
from listarTareasProximasAVencer import listarTareasProximasAVencer


# ─────────────────────────────────────────────
#  PRUEBAS: actualizarEstadoTarea
# ─────────────────────────────────────────────
class TestActualizarEstadoTarea(unittest.TestCase):

    def setUp(self):
        self.tareas_db = {
            "AB123": {
                "id": "AB123",
                "titulo": "Aprobar QA",
                "descripcion": "Estudiar testing",
                "prioridad": "ALTA",
                "estado": "PENDIENTE",
                "fecha_vencimiento": date(2026, 5, 10),
            }
        }

    # CA-01: Cambio de estado válido (PENDIENTE → EN_PROGRESO)
    @patch('builtins.input', side_effect=['AB123', 'EN_PROGRESO'])
    @patch('actualizarEstadoTarea.guardar_tareas')
    def test_01_actualizar_estado_en_progreso(self, mock_guardar, mock_input):
        actualizarEstadoTarea(self.tareas_db)
        self.assertEqual(self.tareas_db['AB123']['estado'], 'EN_PROGRESO')

    # CA-02: Cambio de estado válido (PENDIENTE → COMPLETADA)
    @patch('builtins.input', side_effect=['AB123', 'COMPLETADA'])
    @patch('actualizarEstadoTarea.guardar_tareas')
    def test_02_actualizar_estado_completada(self, mock_guardar, mock_input):
        actualizarEstadoTarea(self.tareas_db)
        self.assertEqual(self.tareas_db['AB123']['estado'], 'COMPLETADA')

    # CA-03: ID no encontrado → mensaje de error y sin cambios
    @patch('builtins.input', side_effect=['ZZ999', 'COMPLETADA'])
    @patch('sys.stdout', new_callable=StringIO)
    @patch('actualizarEstadoTarea.guardar_tareas')
    def test_03_actualizar_estado_id_inexistente(self, mock_guardar, mock_stdout, mock_input):
        actualizarEstadoTarea(self.tareas_db)
        self.assertIn("No se encontró ninguna tarea con el ID 'ZZ999'", mock_stdout.getvalue())
        self.assertEqual(self.tareas_db['AB123']['estado'], 'PENDIENTE')

    # CA-04: Estado inválido → mensaje de error y sin cambios
    @patch('builtins.input', side_effect=['AB123', 'CANCELADA'])
    @patch('sys.stdout', new_callable=StringIO)
    @patch('actualizarEstadoTarea.guardar_tareas')
    def test_04_actualizar_estado_invalido(self, mock_guardar, mock_stdout, mock_input):
        actualizarEstadoTarea(self.tareas_db)
        self.assertIn("Estado inválido", mock_stdout.getvalue())
        self.assertEqual(self.tareas_db['AB123']['estado'], 'PENDIENTE')

    # CA-05: ID vacío → mensaje de error
    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=StringIO)
    @patch('actualizarEstadoTarea.guardar_tareas')
    def test_05_actualizar_estado_id_vacio(self, mock_guardar, mock_stdout, mock_input):
        actualizarEstadoTarea(self.tareas_db)
        self.assertIn("Debes ingresar un ID", mock_stdout.getvalue())

    # CA-06: Confirmación de éxito en consola
    @patch('builtins.input', side_effect=['AB123', 'COMPLETADA'])
    @patch('sys.stdout', new_callable=StringIO)
    @patch('actualizarEstadoTarea.guardar_tareas')
    def test_06_actualizar_muestra_confirmacion(self, mock_guardar, mock_stdout, mock_input):
        actualizarEstadoTarea(self.tareas_db)
        self.assertIn("actualizado a 'COMPLETADA'", mock_stdout.getvalue())


# ─────────────────────────────────────────────
#  PRUEBAS: listarTareasPorPrioridad
# ─────────────────────────────────────────────
class TestListarTareasPorPrioridad(unittest.TestCase):

    def setUp(self):
        self.tareas_db = {
            "AB123": {
                "id": "AB123",
                "titulo": "Tarea Alta",
                "descripcion": "Urgente",
                "prioridad": "ALTA",
                "estado": "PENDIENTE",
                "fecha_vencimiento": date(2026, 5, 10),
            },
            "CD456": {
                "id": "CD456",
                "titulo": "Tarea Media",
                "descripcion": "Normal",
                "prioridad": "MEDIA",
                "estado": "EN_PROGRESO",
                "fecha_vencimiento": date(2026, 6, 1),
            },
            "EF789": {
                "id": "EF789",
                "titulo": "Tarea Baja",
                "descripcion": "Sin prisa",
                "prioridad": "BAJA",
                "estado": "PENDIENTE",
                "fecha_vencimiento": date(2026, 12, 31),
            },
        }

    # CA-07: Tarea de prioridad ALTA aparece en su sección
    @patch('sys.stdout', new_callable=StringIO)
    def test_07_listar_muestra_seccion_alta(self, mock_stdout):
        listarTareasPorPrioridad(self.tareas_db)
        salida = mock_stdout.getvalue()
        self.assertIn("Prioridad ALTA", salida)
        self.assertIn("Tarea Alta", salida)

    # CA-08: Tarea de prioridad MEDIA aparece en su sección
    @patch('sys.stdout', new_callable=StringIO)
    def test_08_listar_muestra_seccion_media(self, mock_stdout):
        listarTareasPorPrioridad(self.tareas_db)
        self.assertIn("Tarea Media", mock_stdout.getvalue())

    # CA-09: Tarea de prioridad BAJA aparece en su sección
    @patch('sys.stdout', new_callable=StringIO)
    def test_09_listar_muestra_seccion_baja(self, mock_stdout):
        listarTareasPorPrioridad(self.tareas_db)
        self.assertIn("Tarea Baja", mock_stdout.getvalue())

    # CA-10: Sección vacía muestra mensaje "(Sin tareas en este nivel)"
    @patch('sys.stdout', new_callable=StringIO)
    def test_10_listar_seccion_vacia(self, mock_stdout):
        del self.tareas_db["EF789"]
        del self.tareas_db["CD456"]
        listarTareasPorPrioridad(self.tareas_db)
        self.assertIn("Sin tareas en este nivel", mock_stdout.getvalue())

    # CA-11: Sin tareas registradas → mensaje de error
    @patch('sys.stdout', new_callable=StringIO)
    def test_11_listar_sin_tareas(self, mock_stdout):
        listarTareasPorPrioridad({})
        self.assertIn("No hay tareas registradas", mock_stdout.getvalue())

    # CA-12: Las tres secciones siempre aparecen aunque estén vacías
    @patch('sys.stdout', new_callable=StringIO)
    def test_12_listar_muestra_tres_secciones(self, mock_stdout):
        listarTareasPorPrioridad(self.tareas_db)
        salida = mock_stdout.getvalue()
        self.assertIn("Prioridad ALTA", salida)
        self.assertIn("Prioridad MEDIA", salida)
        self.assertIn("Prioridad BAJA", salida)


# ─────────────────────────────────────────────
#  PRUEBAS: listarTareasProximasAVencer
# ─────────────────────────────────────────────
class TestListarTareasProximasAVencer(unittest.TestCase):

    def setUp(self):
        hoy = date.today()
        self.tareas_db = {
            "AB123": {
                "id": "AB123",
                "titulo": "Vence en 3 días",
                "descripcion": "Próxima",
                "prioridad": "ALTA",
                "estado": "PENDIENTE",
                "fecha_vencimiento": hoy + timedelta(days=3),
            },
            "CD456": {
                "id": "CD456",
                "titulo": "Vence en 10 días",
                "descripcion": "Lejana",
                "prioridad": "BAJA",
                "estado": "PENDIENTE",
                "fecha_vencimiento": hoy + timedelta(days=10),
            },
            "EF789": {
                "id": "EF789",
                "titulo": "Vence hoy",
                "descripcion": "Urgente",
                "prioridad": "ALTA",
                "estado": "EN_PROGRESO",
                "fecha_vencimiento": hoy,
            },
        }

    # CA-13: Tarea que vence hoy (0 días) aparece en la lista
    @patch('sys.stdout', new_callable=StringIO)
    def test_13_vence_hoy_incluida(self, mock_stdout):
        listarTareasProximasAVencer(self.tareas_db, dias=7)
        self.assertIn("Vence hoy", mock_stdout.getvalue())

    # CA-14: Tarea dentro del rango aparece en la lista
    @patch('sys.stdout', new_callable=StringIO)
    def test_14_vence_en_rango_incluida(self, mock_stdout):
        listarTareasProximasAVencer(self.tareas_db, dias=7)
        self.assertIn("Vence en 3 días", mock_stdout.getvalue())

    # CA-15: Tarea fuera del rango NO aparece en la lista
    @patch('sys.stdout', new_callable=StringIO)
    def test_15_vence_fuera_de_rango_excluida(self, mock_stdout):
        listarTareasProximasAVencer(self.tareas_db, dias=7)
        self.assertNotIn("Vence en 10 días", mock_stdout.getvalue())

    # CA-16: Sin tareas próximas → mensaje informativo
    @patch('sys.stdout', new_callable=StringIO)
    def test_16_sin_tareas_proximas(self, mock_stdout):
        hoy = date.today()
        tareas_lejanas = {
            "ZZ999": {
                "id": "ZZ999",
                "titulo": "Lejana",
                "descripcion": "No vence pronto",
                "prioridad": "BAJA",
                "estado": "PENDIENTE",
                "fecha_vencimiento": hoy + timedelta(days=30),
            }
        }
        listarTareasProximasAVencer(tareas_lejanas, dias=7)
        self.assertIn("No hay tareas que venzan", mock_stdout.getvalue())

    # CA-17: Sin tareas registradas → mensaje de error
    @patch('sys.stdout', new_callable=StringIO)
    def test_17_sin_tareas_registradas(self, mock_stdout):
        listarTareasProximasAVencer({}, dias=7)
        self.assertIn("No hay tareas registradas", mock_stdout.getvalue())

    # CA-18: Resultado ordenado por días restantes (más urgente primero)
    @patch('sys.stdout', new_callable=StringIO)
    def test_18_resultado_ordenado_por_urgencia(self, mock_stdout):
        listarTareasProximasAVencer(self.tareas_db, dias=7)
        salida = mock_stdout.getvalue()
        pos_hoy = salida.find("Vence hoy")
        pos_tres = salida.find("Vence en 3 días")
        self.assertLess(pos_hoy, pos_tres)

    # CA-19: El conteo de resultados es correcto
    @patch('sys.stdout', new_callable=StringIO)
    def test_19_conteo_de_resultados_correcto(self, mock_stdout):
        listarTareasProximasAVencer(self.tareas_db, dias=7)
        self.assertIn("2 tarea(s) próximas", mock_stdout.getvalue())

    # CA-20: Parámetro de días personalizado funciona correctamente
    @patch('sys.stdout', new_callable=StringIO)
    def test_20_parametro_dias_personalizado(self, mock_stdout):
        listarTareasProximasAVencer(self.tareas_db, dias=15)
        self.assertIn("Vence en 10 días", mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
