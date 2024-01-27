class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def postfix_conversion(self, infix):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        postfix = []
        operators = Stack()

        for char in infix:
            if char.isalnum():
                postfix.append(char)
            elif char == '(':
                operators.push(char)
            elif char == ')':
                while not operators.is_empty() and operators.peek() != '(':
                    postfix.append(operators.pop())
                operators.pop()
            else:
                while not operators.is_empty() and precedence.get(char, 0) <= precedence.get(operators.peek(), 0):
                    postfix.append(operators.pop())
                operators.push(char)

        while not operators.is_empty():
            postfix.append(operators.pop())

        return ''.join(postfix)

    def evaluate_postfix(self, postfix):
        operands = Stack()

        for char in postfix:
            if char.isdigit():
                operands.push(int(char))
            else:
                operand2 = operands.pop()
                operand1 = operands.pop()
                if char == '+':
                    operands.push(operand1 + operand2)
                elif char == '-':
                    operands.push(operand1 - operand2)
                elif char == '*':
                    operands.push(operand1 * operand2)
                elif char == '/':
                    operands.push(operand1 // operand2)
                elif char == '^':
                    operands.push(operand1 ** operand2)

        return operands.pop()


if __name__ == "__main__":

    S = Stack()
    infix_expression = "8-2+4*(1+6)+9"
    print("Infix Expression :",infix_expression)

    postfix_expression = S.postfix_conversion(infix_expression)
    print("Postfix Expression:", postfix_expression)

    result = S.evaluate_postfix(postfix_expression)
    print("Result of evaluation:", result)
