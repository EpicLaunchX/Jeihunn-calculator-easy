import pytest

from pytemplate.domain.models import Operands


def test_operands_valid_integers():
    """
    Creating Operands with valid integers should succeed and store values correctly.
    """
    a = Operands(first_operand=5, second_operand=10)
    assert a.first_operand == 5
    assert a.second_operand == 10


@pytest.mark.parametrize(
    "invalid_first, invalid_second",
    [
        ("5", 3),  # first_operand is str, second_operand is int
        (3, "7"),  # first_operand is int, second_operand is str
        (None, 2),  # first_operand is NoneType
        (2, 3.14),  # second_operand is float
        ([], 1),  # first_operand is list
    ],
)
def test_operands_invalid_types_raise_type_error(invalid_first, invalid_second):
    """
    Providing non-int values for operands should raise TypeError.
    """
    with pytest.raises(TypeError):
        Operands(first_operand=invalid_first, second_operand=invalid_second)


def test_operands_repr_contains_fields():
    """
    The auto-generated __repr__ should include class name and field values.
    """
    a = Operands(5, 10)
    text = repr(a)
    assert "Operands" in text
    assert "first_operand=5" in text
    assert "second_operand=10" in text
