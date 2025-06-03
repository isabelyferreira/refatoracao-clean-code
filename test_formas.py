import unittest
from formas import Quadrado, Retangulo, Circulo


class TestFormas(unittest.TestCase):
    def test_area_quadrado(self):
        quadrado = Quadrado(4)
        self.assertEqual(quadrado.calcular_area(), 16)

    def test_area_retangulo(self):
        retangulo = Retangulo(4, 5)
        self.assertEqual(retangulo.calcular_area(), 20)

    def test_area_circulo(self):
        circulo = Circulo(3)
        self.assertAlmostEqual(circulo.calcular_area(), 28.274, places=3)


if __name__ == "__main__":
    unittest.main()