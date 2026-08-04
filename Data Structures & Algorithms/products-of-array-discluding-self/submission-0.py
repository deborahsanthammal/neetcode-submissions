class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_array = [0] * len(nums)
        postfix_array = [0] * len(nums)
        output = []

        i = 1 
        prefix_array[0] = nums[0]
        while i < len(nums):
            prefix_array[i] = prefix_array[i-1] * nums[i]
            i += 1

        i = len(nums) - 2
        postfix_array[len(nums)-1] = nums[len(nums)-1]
        while i >= 0:
            postfix_array[i] = postfix_array[i+1] * nums[i]
            i -= 1
        i = 0
        while i < len(nums):
            prefix = 1 if i == 0 else prefix_array[i-1]
            postfix = 1 if i == len(nums) - 1 else postfix_array[i+1]
            output.append(prefix * postfix)
            i += 1

        return output
