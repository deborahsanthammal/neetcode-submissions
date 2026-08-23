class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        output = [0] * len(temperatures) 
        for index, element in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < element:
                top = stack.pop()
                difference = index - top
                output[top] = difference

            stack.append(index)

        return output

        