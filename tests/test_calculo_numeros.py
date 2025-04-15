
import unittest
from src.exceptions import (
    ingrese_numero,
    NumeroDebeSerPositivo,
)
from unittest.mock import patch

class TestCalculoNumeros(unittest.TestCase):

    @patch(  # este patch controla lo que hace el input
        'builtins.input',
        return_value='100'
    )
    def test_ingreso_feliz(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 100)

    @patch('builtins.input', return_value='42')
    def test_ingreso_feliz_42(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 42)

    @patch('builtins.input', return_value='2000')
    def test_ingreso_feliz_2000(self, patch_input):
        numero = ingrese_numero()
        self.assertEqual(numero, 2000)

if __name__ == '__main__':
    unittest.main() 