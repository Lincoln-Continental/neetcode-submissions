class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "/", "*"}

        for token in tokens:
            if token in operations:
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "/":
                    stack.append(int(a/b))
                elif token == "*":
                    stack.append(a*b)
            else:
                stack.append(int(token))
        return stack[-1]