class BT:
    def GiaTri(self, bt):
        operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

        def evaluate(operands, operators):
            while operators:
                op = operators.pop()
                right = operands.pop()
                left = operands.pop()
                operands.append(op(left, right))
            return operands.pop()

        operands_stack = []
        operators_stack = []

        i = 0
        while i < len(bt):
            if bt[i].isdigit():
                operand = 0
                while i < len(bt) and bt[i].isdigit():
                    operand = operand * 10 + int(bt[i])
                    i += 1
                operands_stack.append(operand)
            elif bt[i] == '(':
                operators_stack.append(bt[i])
                i += 1
            elif bt[i] == ')':
                while operators_stack and operators_stack[-1] != '(':
                    op = operators_stack.pop()
                    right = operands_stack.pop()
                    left = operands_stack.pop()
                    operands_stack.append(operators[op](left, right))
                operators_stack.pop()  # Pop '('
                i += 1
            else:
                while operators_stack and precedence[bt[i]] <= precedence[operators_stack[-1]]:
                    op = operators_stack.pop()
                    right = operands_stack.pop()
                    left = operands_stack.pop()
                    operands_stack.append(operators[op](left, right))
                operators_stack.append(bt[i])
                i += 1

        while operators_stack:
            op = operators_stack.pop()
            right = operands_stack.pop()
            left = operands_stack.pop()
            operands_stack.append(operators[op](left, right))

        return operands_stack[0]
