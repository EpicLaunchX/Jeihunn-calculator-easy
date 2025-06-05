from pytemplate.domain.models import Operands


class Calculator:
    """
    Calculator service that performs basic arithmetic operations
    on an Operands instance. All methods return an int.
    """

    def add(self, operands: Operands) -> int:
        """
        Return the sum of first_operand and second_operand.
        """
        return operands.first_operand + operands.second_operand

    def subtract(self, operands: Operands) -> int:
        """
        Return the difference: first_operand minus second_operand.
        """
        return operands.first_operand - operands.second_operand

    def multiply(self, operands: Operands) -> int:
        """
        Return the product of first_operand and second_operand.
        """
        return operands.first_operand * operands.second_operand

    def divide(self, operands: Operands) -> int:
        """
        Return the integer division result of first_operand by second_operand.
        Raises ZeroDivisionError if second_operand is zero.
        """
        return operands.first_operand // operands.second_operand
