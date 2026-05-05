import unittest
from unittest.mock import patch
from io import StringIO
from datetime import datetime
from buscarTareaPorId import buscarTareaPorId

class TestBuscarTarea(unittest.TestCase):

    def setUp(self):
        self.tareas_db = {
            "AB123": {
                "id": "AB123",
                "titulo": "Aprobar QA",
                "descripcion": "Estudiar testing",
                "prioridad": "ALTA",
                "fecha_vencimiento": datetime(2026, 5, 10).date()
            }
        }

    @patch('builtins.input', side_effect=['AB123'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_01_buscar_tarea_existente(self, mock_stdout, mock_input):
        buscarTareaPorId(self.tareas_db)
        self.assertIn("Aprobar QA", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['ZZ999'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_02_buscar_tarea_inexistente(self, mock_stdout, mock_input):
        buscarTareaPorId(self.tareas_db)
        self.assertIn("No se encontró ninguna tarea", mock_stdout.getvalue())

    @patch('builtins.input', side_effect=['ZZ999'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_03_buscar_tarea_50000_registros(self, mock_stdout, mock_input):
        for i in range(50000):
            id_gen = f"XX{str(i).zfill(3)}"
            self.tareas_db[id_gen] = {
                "id": id_gen,
                "titulo": "Tarea automatizada",
                "descripcion": "Carga de estres",
                "prioridad": "BAJA",
                "fecha_vencimiento": datetime(2026, 12, 31).date()
            }
        
        self.tareas_db["ZZ999"] = { 
            "id": "ZZ999",
            "titulo": "Evaluacion de rendimiento",
            "descripcion": "Prueba SPICE",
            "prioridad": "ALTA",
            "fecha_vencimiento": datetime(2026, 5, 10).date()
        }

        buscarTareaPorId(self.tareas_db)
        self.assertIn("Evaluacion de rendimiento", mock_stdout.getvalue())

if __name__ == '__main__':
    unittest.main()