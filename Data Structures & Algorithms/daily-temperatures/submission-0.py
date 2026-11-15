class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in range(len(temperatures))]
        stack = [(temperatures[0], 0)]
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                t, index = stack.pop()
                res[index] = i - index
            stack.append((temperatures[i], i))
        return res
            