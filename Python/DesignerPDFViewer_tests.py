import unittest
import DesignerPDFViewer


class pdfSelectionTests(unittest.TestCase):

    def test1(self):
        testWeights = '1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5'
        h = map(int, testWeights.strip().split(' '))
        word = 'abc'
        self.assertEqual(DesignerPDFViewer.pdfSelection(h, word), 9)

if __name__ == "__main__":
    unittest.main()
