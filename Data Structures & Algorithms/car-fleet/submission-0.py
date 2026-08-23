class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        stack = []
        for p, s in zip(position, speed):
            pair.append([p,s])

        reverse_order = sorted(pair, reverse=True)

        for p, s in reverse_order:
            distance = (target - p) / s
            stack.append(distance)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)