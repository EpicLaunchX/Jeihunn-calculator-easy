import pytest

from pytemplate.domain.models import Operands, operands_factory
from pytemplate.service.calculator import Calculator


@pytest.mark.parametrize(
    "first, second, expected",
    [
        (5, 3, 8),  # 5 + 3 = 8
        (0, 0, 0),  # 0 + 0 = 0
        (-2, 7, 5),  # -2 + 7 = 5
        (10, -4, 6),  # 10 + (-4) = 6
    ],
)
def test_add(first, second, expected):
    calc = Calculator()
    ops = operands_factory(first, second)
    result = calc.add(ops)
    assert isinstance(result, int)
    assert result == expected


@pytest.mark.parametrize(
    "first, second, expected",
    [
        (10, 3, 7),  # 10 - 3 = 7
        (0, 0, 0),  # 0 - 0 = 0
        (-5, -2, -3),  # -5 - (-2) = -3
        (4, 10, -6),  # 4 - 10 = -6
    ],
)
def test_subtract(first, second, expected):
    calc = Calculator()
    ops = operands_factory(first, second)
    result = calc.subtract(ops)
    assert isinstance(result, int)
    assert result == expected


@pytest.mark.parametrize(
    "first, second, expected",
    [
        (2, 3, 6),
        (0, 5, 0),
        (-2, 4, -8),
        (7, -3, -21),
    ],
)
def test_multiply(first, second, expected):
    calc = Calculator()
    ops = operands_factory(first, second)
    result = calc.multiply(ops)
    assert isinstance(result, int)
    assert result == expected


@pytest.mark.parametrize(
    "first, second, expected",
    [
        (10, 2, 5),  # 10 // 2 = 5
        (9, 4, 2),  # 9 // 4 = 2 (floor division)
        (-8, 2, -4),  # -8 // 2 = -4
        (7, -3, -3),  # 7 // (-3) = -3 (floor division)
    ],
)
def test_divide(first, second, expected):
    calc = Calculator()
    ops = operands_factory(first, second)
    result = calc.divide(ops)
    assert isinstance(result, int)
    assert result == expected


def test_divide_by_zero():
    calc = Calculator()
    ops = operands_factory(5, 0)
    with pytest.raises(ZeroDivisionError):
        calc.divide(ops)
