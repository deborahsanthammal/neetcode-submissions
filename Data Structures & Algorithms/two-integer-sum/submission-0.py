class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in n:
                return [n[difference], i]
            else:
                n[nums[i]] = i 