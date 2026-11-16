class Solution:
    def trap(self, height: List[int]) -> int:
        s = 0 
        max_right = [0 for i in range(len(height))]
        for r in range(1, len(height)):
            #print(r)
            max_right[len(height) - r - 1] = max(height[len(height) - r], max_right[len(height) - r])
        
        l = 0
        for i in range(len(height)):
            if height[i] > l:
                l = height[i]
            s += max(0, min(l, max_right[i]) - height[i])
        return s