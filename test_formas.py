
import unittest
from formas import Quadrado, Retangulo, Circulo, FormaFactory

class TestFormas(unittest.TestCase):
    def test_quadrado(self):
        q = Quadrado(4)
        self.assertEqual(q.calcular_area(), 16)

    def test_retangulo(self):
        r = Retangulo(4, 5)
        self.assertEqual(r.calcular_area(), 20)

    def test_circulo(self):
        c = Circulo(3)
        self.assertAlmostEqual(c.calcular_area(), 28.274, places=3)

    def test_factory(self):
        q = FormaFactory.criar_forma('quadrado', 4)
        self.assertIsInstance(q, Quadrado)
        r = FormaFactory.criar_forma('retangulo', 4, 5)
        self.assertIsInstance(r, Retangulo)
        c = FormaFactory.criar_forma('circulo', 3)
        self.assertIsInstance(c, Circulo)

    def test_factory_invalid(self):
        with self.assertRaises(ValueError):
            FormaFactory.criar_forma('triangulo', 3, 4)

if __name__ == '__main__':
    unittest.main()
