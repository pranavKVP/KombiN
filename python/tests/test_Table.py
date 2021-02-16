
import unittest
from kombin import Table


class TableTest(unittest.TestCase):

    def test_all_30_false(self):
        result = True
        for X in range(1, 31):
            for Y in range(1, 31):
                _X_Y = Table(X, Y, False)
                for i in range(1, (X * Y) + 1):
                    ai, bi = _X_Y.GetElementsAtIndex(i)
                    index = _X_Y.GetIndexOfElements(ai, bi)
                    if(i != index):
                        result = False
        self.assertEqual(result, True)

    def test_all_30_true(self):
        result = True
        for X in range(1, 31):
            for Y in range(1, 31):
                _X_Y = Table(X, Y, True)
                for i in range(0, (X * Y)):
                    ai, bi = _X_Y.GetElementsAtIndex(i)
                    index = _X_Y.GetIndexOfElements(ai, bi)
                    if(i != index):
                        result = False
        self.assertEqual(result, True)
