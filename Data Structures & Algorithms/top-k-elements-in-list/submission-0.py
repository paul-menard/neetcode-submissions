from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        vals = [(key, value) for key, value in d.items()]
        vals.sort(key = (lambda x : x[1]))
        res = []
        for i in range(k):
            res.append(vals.pop()[0])
        return res