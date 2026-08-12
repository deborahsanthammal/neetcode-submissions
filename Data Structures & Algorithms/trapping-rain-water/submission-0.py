class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        max_l = height[0]
        max_r = height[len(height)-1]
        total_water = 0
        while l < r:
            if max_l > max_r:
                r -= 1
                water = max(max_r, height[r]) - height[r] if max(max_r, height[r]) - height[r] > 0 else 0
                max_r = max(max_r, height[r])
                total_water += water
                
            else:
                l += 1
                water = max(max_l, height[l]) - height[l] if max(max_l, height[l]) - height[l] > 0 else 0
                max_l = max(max_l, height[l])
                total_water += water
                

        return total_water