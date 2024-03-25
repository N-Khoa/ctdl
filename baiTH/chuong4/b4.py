class BT:
    def HauTo(self, bt):
        operators = {'+': 1, '-': 1, '*': 2, '/': 2}
        hauto = []
        operators_stack = []

        i = 0
        while i < len(bt):
            if bt[i].isdigit():
                operand = ''
                while i < len(bt) and bt[i].isdigit():
                    operand += bt[i]
                    i += 1
                hauto.append(operand)
            elif bt[i] == '(':
                operators_stack.append(bt[i])
                i += 1
            elif bt[i] == ')':
                while operators_stack and operators_stack[-1] != '(':
                    hauto.append(operators_stack.pop())
                operators_stack.pop()  # Pop '('
                i += 1
            else:
                while operators_stack and operators_stack[-1] != '(' and operators[bt[i]] <= operators[operators_stack[-1]]:
                    hauto.append(operators_stack.pop())
                operators_stack.append(bt[i])
                i += 1

        while operators_stack:
            hauto.append(operators_stack.pop())

        return ' '.join(hauto)

