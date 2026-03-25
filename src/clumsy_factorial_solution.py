# Recursive functions execute by first reaching the base case through recursive calls, 
# then unwinding the call stack while applying operations in reverse order. 
# E.g. factorial(5) would be computed as follows:
# 
# 5 × factorial(4)
#   → 5 × (4 × factorial(3))
#      → 5 × (4 × (3 × factorial(2)))
#         → 5 × (4 × (3 × (2 × factorial(1))))
#            → 5 × (4 × (3 × (2 × 1)))
#            → 5 × (4 × (3 × 2))
#            → 5 × (4 × 6)
#            → 5 × 24
#            → 120   
# 
# However, this would not apply the usual order of operations of arithmetic, i.e. all multiplication and division steps before 
# any addition or subtraction steps, and multiplication and division steps are processed left to right.


from operator import mul, floordiv, add, sub
from collections import deque

class ClumsyFactorialSolution:

    # Index order in this tuple is important for generating clumsy factorial expresion.
    operators = (mul, floordiv, add, sub)
    stack = deque()

    def clumsy(self, n: int) -> int:
        self.build_calculation_and_apply_multiplicatives(n)

	    # Reverse the stack so operations are applied left to right.
        self.stack.reverse()
        result = self.apply_addition_subtraction()
        
        return result

    # It would be cleaner code to first build the calculation and then apply multiplcation and division in two separate 
    # functions, but this reduces the steps by applying multiplcation and division while building the remaining
    # add/subtract calculation.
    def build_calculation_and_apply_multiplicatives(self, n: int, current_op_index: int = 0) -> None:

        if n == 1:
            if not self.is_top_element_an_int():
                self.stack.append(1)

        elif n != 1:
            if current_op_index > 3:
                current_op_index = 0

            current_operator = self.operators[current_op_index]

            if len(self.stack) == 0:
                self.stack.append(n)

            if current_operator == mul or current_operator == floordiv:
                self.apply_multiplication_and_division(n ,current_operator)
            elif current_operator == add:
                self.stack.append(current_operator)
            else:
                self.stack.append(n)
                self.stack.append(current_operator)

            self.build_calculation_and_apply_multiplicatives(n - 1, current_op_index + 1)

    def apply_multiplication_and_division(self, n: int, current_operator) -> None:
        result = 0
        if self.is_top_element_an_int():
            result = current_operator(self.stack.pop(), n -1 )
        else:
            result = current_operator(n, n -1 )
        
        self.stack.append(result)
    
    def apply_addition_subtraction(self, result:int = 0) -> int:

        if len(self.stack) == 0:
            return result

        if self.is_top_element_an_int():
            left_value = self.stack.pop()
        else:
            left_value = result

        operator = self.stack.pop()
        right_value = self.stack.pop()

        if not isinstance(left_value, int):
            raise ValueError("left_value must be an int.")
        if not isinstance(right_value, int):
            raise ValueError("right_value must be an int.")
        if isinstance(operator, int):
            raise ValueError("operator must not be an int.")

        result = operator(left_value, right_value)

        return self.apply_addition_subtraction(result)
    
    def is_top_element_an_int(self) -> bool:
	    return isinstance(self.stack[-1], int)