from dataclasses import dataclass


@dataclass
class Operands:
    first_operand: int
    second_operand: int

    def __post_init__(self):
        if not isinstance(self.first_operand, int):
            raise TypeError(f"first_operand must be int, got {type(self.first_operand).__name__}")
        if not isinstance(self.second_operand, int):
            raise TypeError(f"second_operand must be int, got {type(self.second_operand).__name__}")


def operands_factory(first_operand: int, second_operand: int) -> Operands:
    return Operands(first_operand=first_operand, second_operand=second_operand)
