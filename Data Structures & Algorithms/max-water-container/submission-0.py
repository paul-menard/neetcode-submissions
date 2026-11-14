class Solution:
    def maxArea(self, heights: List[int]) -> int:

        ## the area is min(l,r)*(r-l)
        ## we just iterate over the possibilities
        ## we increment on the side of the smallest one
        n = len(heights)
        l = 0
        r = n-1
        max_area = 0
        while l < r : 
            if min(heights[l], heights[r])*(r-l) > max_area:
                max_area = min(heights[l], heights[r])*(r-l)
            if heights[l] <= heights[r] :
                l += 1
            else :
                r -= 1
        return max_area
        