import unittest
import DesignerPDFViewer


class pdfSelectionTests(unittest.TestCase):

    def test1(self):
        h = "1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5"
        word = "abc"
        self.assertEqual(DesignerPDFViewer.pdfSelection(h, word), 9)

if __name__ == "__main__":
    unittest.main()
