from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            l = [0]*26
            for letter in s:
                l[ord(letter)-ord("a")] += 1
            d[tuple(l)].append(s)
        return list(d.values())