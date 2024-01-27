class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.top.data

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
    infix_expression = "7+(5/9)-6+(4*9)+8"
    print("Infix Expression :",infix_expression)

    postfix_expression = S.postfix_conversion(infix_expression)
    print("Postfix Expression:", postfix_expression)

    result = S.evaluate_postfix(postfix_expression)
    print("Result of Evaluation:", result)
