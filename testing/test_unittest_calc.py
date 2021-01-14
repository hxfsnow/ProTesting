import unittest

from python.calc import Calc

import  sys
sys.path.append('..')
# print(sys.path)
class TestCalc(unittest.TestCase):
    def test_add_1(self):
        self.calc = Calc()
        result = self.calc.add(1, 2)
        self.assertEqual(3,result)
unittest.main()