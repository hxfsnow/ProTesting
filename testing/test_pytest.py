'''
设计测试用例，需考虑：正数，负数，0，大数，小数
'''

import pytest
from python.calc import Calc


class TestCalc:
    def setup(self):
        self.calc = Calc()
    @pytest.mark.parametrize("a,b,expected",[(-1,-1,-2),(2,3,5),(0.1,0.5,0.6)])
    def test_add_1(self,a,b,expected):
        result = self.calc.add(a, b)
        assert expected == result

    @pytest.mark.parametrize("a,b,expected", [(4,0,0),(-1,-1,1), (6,3,2), (0.5,0.1,5),(6,5,1.2)])
    def test_div_2(self,a,b,expected):
        try:
            result = self.calc.div(a, b)
        except:
            return "Divided can not be zero!"
        assert expected == result


if __name__ == '__main__': # python的入口函数
    pytest.main()
