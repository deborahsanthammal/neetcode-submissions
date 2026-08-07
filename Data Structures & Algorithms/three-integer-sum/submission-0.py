class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        i = 0
        for i , _ in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == 0:
                    output.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j+= 1
                elif sum > 0:
                    k -= 1
                else:
                    j+=1
            
        return output