import unittest
from KombiN import KombiN


class KombiNTest(unittest.TestCase):

    def test_all_30_false(self):
        result = True
        for X in range(1, 31):
            for Y in range(1, 31):
                _X_Y = KombiN(X, Y, False)
                for i in range(1, (X * Y) + 1):
                    Ai, Bi = _X_Y.GetCombination(i)
                    index = _X_Y.GetIndex(Ai, Bi)
                    if(i != index):
                        # result = False
                        raise ValueError(f"i:{i}#index{index} for Ai:{Ai}, Bi:{Bi}")
        self.assertEqual(result, True)

    def test_all_30_true(self):
        result = True
        for X in range(1, 31):
            for Y in range(1, 31):
                _X_Y = KombiN(X, Y, True)
                for i in range(0, (X * Y)):
                    Ai, Bi = _X_Y.GetCombination(i)
                    index = _X_Y.GetIndex(Ai, Bi)
                    if(i != index):
                        # result = False
                        raise ValueError(f"i:{i}#index{index} for Ai:{Ai}, Bi:{Bi}")
        self.assertEqual(result, True)
