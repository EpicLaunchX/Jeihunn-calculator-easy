from pytemplate.domain.models import operands_factory
from pytemplate.service.calculator import Calculator


def main() -> int:
    first = int(input("Enter first operand: ").strip())
    second = int(input("Enter second operand: ").strip())
    action = input("Enter action (add, subtract, multiply, divide): ").strip().lower()

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


if __name__ == "__main__":
    try:
        result = main()
        print(f"Result: {result}")
    except Exception as e:
        print(f"Error: {e}")
        exit(1)
