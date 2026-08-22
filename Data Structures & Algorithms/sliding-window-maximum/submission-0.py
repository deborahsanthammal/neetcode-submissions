class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        output = []
        l = 0
        for r in range(len(nums)):
            if dq and dq[0] <= (r - k):
                dq.popleft()

            while dq and nums[dq[-1]] < nums[r]:
                dq.pop()

            dq.append(r)

            if r >= k-1:
                output.append(nums[dq[0]])
                l += 1

        return output