import pytest

from python.calc import Calc


class TestCalc:
    """
        1.两个整数
        2.两个负数
        3.一正一负
        4.0和整数
        5.0和负数
        6.均为0
        7.两个大数据
        8.两个小数
        9.整数和小数
    """
    @pytest.mark.parametrize("a, b, result",[
        (10,20,30),
        (-10,-20,-30),
        (10,-20,-10),
        (0,10,10),
        (0,-10,-10),
        (0, 0, 0),
        (1000,3000,4000),
        (0.03, 0.13, 0.16),
        (10, 0.56, 10.56)
    ])
    def test_add(self,a,b,result):
        calc = Calc()
        assert (result, calc.add(a, b))

    """
            1.两个整数
            2.两个负数
            3.一正一负
            4.0和整数
            5.0和负数
            6.均为0(除数为0)
            7.两个大数据
            8.两个小数
            9.整数和小数
        """
    @pytest.mark.parametrize("a, b, result", [
        (21, 2, 10),
        (-10, -20, 0),
        (10, -20, 0),
        (0, 10, 0),
        (0, -10, 0),
        (0, 0, "error"),
        (1000, 3000, 0),
        (0.6,0.3, 2),
        (0.6, 2, 0.3)
    ])
    def test_div(self,a,b,result):
        calc = Calc()
        assert (result, calc.div(a, b))

if __name__ == '__main__':
    pytest.main()