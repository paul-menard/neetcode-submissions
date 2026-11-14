class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, suffix = 1, 1
        res = []
        for i in range(1, len(nums)):
            suffix *= nums[i]
        res.append(prefix*suffix)
        for i in range(1, len(nums)):
            prefix *= nums[i-1]
            if nums[i] != 0:
                suffix *= 1/nums[i]
            else :
                suffix = 1
                for j in range(min(i+1, len(nums)), len(nums)):
                    suffix *= nums[j]
            suffix = int(suffix)
            res.append(prefix*suffix)
        return res
