class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for char in tokens:
            if char == "+" or char == "-" or char == "/" or char == "*":
                val1 = stack.pop()
                val2 = stack.pop()
                if char == "+":
                    stack.append(val2+val1)
                elif char == "-":
                    stack.append(val2-val1)
                elif char == "*":
                    stack.append(val2*val1)
                elif char == "/":
                    stack.append(int(val2/val1))

            else:
                stack.append(int(char))

        return stack[-1]

        