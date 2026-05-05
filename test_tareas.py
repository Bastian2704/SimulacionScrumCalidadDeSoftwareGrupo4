import unittest
from unittest.mock import patch
from io import StringIO
from datetime import datetime
from crearTareas import crearTarea

class TestGestorTareas(unittest.TestCase):

    def setUp(self):
        self.tareas_db = {}

    @patch('builtins.input', side_effect=['AB123', 'Aprobar QA', 'Estudiar testing', 'ALTA', '2026-05-10'])
    @patch('crearTareas.guardar_tareas')
    def test_01_crear_tarea_valida(self, mock_guardar, mock_input):
        crearTarea(self.tareas_db)
        self.assertIn('AB123', self.tareas_db)

    @patch('builtins.input', side_effect=['AB123', 'CD456', 'Aprobar QA', 'Estudiar testing', 'ALTA', '2026-05-10'])
    @patch('sys.stdout', new_callable=StringIO)
    @patch('crearTareas.guardar_tareas')
    def test_02_crear_tarea_id_duplicado(self, mock_guardar, mock_stdout, mock_input):
        self.tareas_db['AB123'] = {"id": "AB123"}
        crearTarea(self.tareas_db)
        self.assertIn("Ya existe una tarea con el ID 'AB123'", mock_stdout.getvalue())
        self.assertIn('CD456', self.tareas_db)

    @patch('builtins.input', side_effect=['12345', 'AB123', 'Aprobar QA', 'Estudiar testing', 'ALTA', '2026-05-10'])
    @patch('sys.stdout', new_callable=StringIO)
    @patch('crearTareas.guardar_tareas')
    def test_03_crear_tarea_id_formato_incorrecto(self, mock_guardar, mock_stdout, mock_input):
        crearTarea(self.tareas_db)
        self.assertIn("El ID debe tener 2 letras seguidas de 3 números", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['AB123', '', 'Aprobar QA', 'Estudiar testing', 'ALTA', '2026-05-10'])
    @patch('sys.stdout', new_callable=StringIO)
    @patch('crearTareas.guardar_tareas')
    def test_04_crear_tarea_titulo_vacio(self, mock_guardar, mock_stdout, mock_input):
        crearTarea(self.tareas_db)
        self.assertIn("El título no puede estar vacío", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['AB123', 'Aprobar QA', '', 'Estudiar testing', 'ALTA', '2026-05-10'])
    @patch('sys.stdout', new_callable=StringIO)
    @patch('crearTareas.guardar_tareas')
    def test_05_crear_tarea_descripcion_vacia(self, mock_guardar, mock_stdout, mock_input):
        crearTarea(self.tareas_db)
        self.assertIn("La descripción no puede estar vacía", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['AB123', 'A' * 105, 'Estudiar testing', 'ALTA', '2026-05-10'])
    @patch('crearTareas.guardar_tareas')
    def test_06_crear_tarea_titulo_largo(self, mock_guardar, mock_input):
        crearTarea(self.tareas_db)
        self.assertEqual(len(self.tareas_db['AB123']['titulo']), 105)

    @patch('builtins.input', side_effect=['AB123', 'Aprobar QA', 'Estudiar testing', 'ALTA', '10/05/2026', '2026-05-10'])
    @patch('sys.stdout', new_callable=StringIO)
    @patch('crearTareas.guardar_tareas')
    def test_07_crear_tarea_fecha_incorrecta(self, mock_guardar, mock_stdout, mock_input):
        crearTarea(self.tareas_db)
        self.assertIn("Formato inválido. Usa YYYY-MM-DD", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main() 