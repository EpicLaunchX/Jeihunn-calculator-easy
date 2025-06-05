import pytest

from pytemplate.domain.models import Operands, operands_factory


def test_operands_factory_returns_operands_instance():
    """
    Creating Operands via factory with valid integers should return an Operands object,
    and its fields should match the inputs.
    """
    # Call the factory
    result = operands_factory(7, 3)

    # Verify that the returned object is an instance of Operands
    assert isinstance(result, Operands)

    # Verify that the fields inside Operands have the correct values
    assert result.first_operand == 7
    assert result.second_operand == 3


@pytest.mark.parametrize(
    "invalid_first, invalid_second",
    [
        ("5", 2),  # first_operand is str
        (2, "10"),  # second_operand is str
        (None, 4),  # first_operand is NoneType
        (1, 2.5),  # second_operand is float
        ([], 0),  # first_operand is list
    ],
)
def test_operands_factory_invalid_types_raise_type_error(invalid_first, invalid_second):
    """
    If either first_operand or second_operand is not an int, the factory
    should cause a TypeError (propagated from the Operands constructor).
    """
    with pytest.raises(TypeError):
        operands_factory(first_operand=invalid_first, second_operand=invalid_second)
