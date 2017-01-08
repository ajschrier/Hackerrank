import Quartiles
import unittest


class Quartiles_tests(unittest.TestCase):
    """docstring for Quartiles_tests"""
    def test1(self):
        self.assertEqual(Quartiles.quartiles(9,
                         [3, 7, 8, 5, 12, 14, 21, 13, 18]),
                         [6, 12, 16])

    def test2(self):
        self.assertEqual(Quartiles.quartiles(10,
                         [3, 7, 8, 5, 12, 14, 21, 15, 18, 14]),
                         [7, 13, 15])


if __name__ == '__main__':
    unittest.main()
