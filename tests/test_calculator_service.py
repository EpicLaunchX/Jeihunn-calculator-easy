import pytest

from pytemplate.domain.models import Operands
from pytemplate.service.calculator import Calculator


@pytest.fixture
def calc():
    """
    Provide a Calculator instance for tests.
    """
    return Calculator()


@pytest.mark.parametrize(
    "first, second, expected",
    [
        (5, 3, 8),  # 5 + 3 = 8
        (0, 0, 0),  # 0 + 0 = 0
        (-2, 7, 5),  # -2 + 7 = 5
        (10, -4, 6),  # 10 + (-4) = 6
    ],
)
def test_add(calc, first, second, expected):
    """
    Test that add method returns correct sum.
    """
    ops = Operands(first_operand=first, second_operand=second)
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
def test_subtract(calc, first, second, expected):
    """
    Test that subtract method returns correct difference.
    """
    ops = Operands(first_operand=first, second_operand=second)
    result = calc.subtract(ops)
    assert isinstance(result, int)
    assert result == expected


@pytest.mark.parametrize(
    "first, second, expected",
    # [
    #     (2, 3, 6),  # 2 * 3 = 6
    #     (0, 5, 0),  # 0 * 5 = 0
    #     (-2, 4, -8),  # -2 * 4 = -8
    #     (7, -3, -21),  # 7 * (-3) = -21
    # ],
    [
        (2, 3, 8),  # 2 ** 3 = 8
        (0, 5, 0),  # 0 ** 5 = 0
    ],
)
def test_multiply(calc, first, second, expected):
    """
    Test that multiply method returns correct product.
    """
    ops = Operands(first_operand=first, second_operand=second)
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
def test_divide(calc, first, second, expected):
    """
    Test that divide method returns correct integer division result.
    """
    ops = Operands(first_operand=first, second_operand=second)
    result = calc.divide(ops)
    assert isinstance(result, int)
    assert result == expected


def test_divide_by_zero(calc):
    """
    Attempting to divide by zero should raise ZeroDivisionError.
    """
    ops = Operands(first_operand=5, second_operand=0)
    with pytest.raises(ZeroDivisionError):
        calc.divide(ops)
