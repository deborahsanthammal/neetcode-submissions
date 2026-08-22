class Solution:
    def isValid(self, s: str) -> bool:
        paranthesis_map = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack = []

        for c in s:
            if c in paranthesis_map:
                if stack and stack[-1] == paranthesis_map[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
