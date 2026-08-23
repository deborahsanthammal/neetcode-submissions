class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
    
        for i in tokens:
            if i in "+-*/":
                operand1 = stack.pop()
                operand2 = stack.pop()

                if i == "+":
                    result = operand2 + operand1
                elif i == "-":
                    result = operand2 - operand1
                elif i == "*":
                    result = operand2 * operand1
                elif i == "/":
                    result = int(operand2 / operand1)

                stack.append(result)
                
            else:
                stack.append(int(i))

        return stack[-1]