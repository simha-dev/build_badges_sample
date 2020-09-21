import pytest
from example.calculator_functions import *

@pytest.mark.parametrize('num1, num2, expected_result',
                    [(10,7,17),
                    (9,4,13),
                    (-100,76,-24),
                    (0,0,0)
                    ])

def test_add(num1,num2,expected_result):
    result = add(num1,num2)
    assert(result==expected_result)


@pytest.mark.parametrize('num1, num2, expected_result',
                    [(10,7,3),
                    (9,4,5),
                    (-100,76,-176),
                    (0,0,0),
                    (5,-8,13)
                    ])
def test_sub(num1,num2,expected_result):
    result = sub(num1,num2)
    assert(result==expected_result)

@pytest.mark.skip(reason="skipped test to show how it works")
def test_sub_abnormal():
    pass


@pytest.mark.parametrize('num1, num2, expected_result',
                    [(5,6,30),
                    (90,-3,-270),
                    (-100,-76,7600),
                    (0,19,0),
                    (-5,8,-40)
                    ])
def test_multiply(num1,num2,expected_result):
    result = multiply(num1,num2)
    assert(result==expected_result)


def test_should_fail():
    assert(100 == 500)

@pytest.mark.parametrize('num1, num2, expected_result',
                    [(9,3,3),
                     (10,2,5)
                    ])
def test_divide_normal(num1,num2,expected_result):
    result = divide(num1,num2)
    assert(result==expected_result)



def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        result = divide(1,0)
        assert(result==expected_result)
