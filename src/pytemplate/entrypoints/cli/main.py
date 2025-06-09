from src.pytemplate.domain.models import operands_factory
from src.pytemplate.service.calculator import Calculator


def main() -> int:
    first = int(input("Enter first operand: "))
    second = int(input("Enter second operand: "))
    action = input("Enter action (add, subtract, multiply, divide): ")

    calc = Calculator()
    operands = operands_factory(first, second)

    if action == "add":
        return calc.add(operands)
    elif action == "subtract":
        return calc.subtract(operands)
    elif action == "multiply":
        return calc.multiply(operands)
    elif action == "divide":
        return calc.divide(operands)
    else:
        raise ValueError("Invalid action. Must be one of: add, subtract, multiply, divide.")
