import InterquartileRange
import unittest


class IQR_tests(unittest.TestCase):

    def test1(self):
        self.assertEqual(InterquartileRange.
                         interQuartileRange([6, 6, 6, 6, 6, 8, 8, 8, 10, 10,
                                            12, 12, 12, 12, 16, 16, 16, 16,
                                            16, 20]), 9.0)

if __name__ == '__main__':
    unittest.main()
