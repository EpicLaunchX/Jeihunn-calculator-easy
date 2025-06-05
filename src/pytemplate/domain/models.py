from dataclasses import dataclass


@dataclass
class Operands:
    """
    A class that holds two operands (first_operand, second_operand) as integers.
    Raises a TypeError if the provided values are not integers.
    """

    first_operand: int
    second_operand: int

    def __post_init__(self):
        # Ensure that first_operand and second_operand are indeed integers
        if not isinstance(self.first_operand, int):
            raise TypeError(f"first_operand must be int, got {type(self.first_operand).__name__}")
        if not isinstance(self.second_operand, int):
            raise TypeError(f"second_operand must be int, got {type(self.second_operand).__name__}")


def operands_factory(first_operand: int, second_operand: int) -> Operands:
    """
    Create and return an Operands instance from two integer arguments.
    Both first_operand and second_operand must be of type int, otherwise
    TypeError will be raised (by the Operands constructor).
    """
    return Operands(first_operand=first_operand, second_operand=second_operand)
