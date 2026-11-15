class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"}" : "{", ")":"(", "]":"["}
        for p in s:
            if p in d.values():
                stack.append(p)
            else :
                if len(stack) > 0 and d[p] == stack[-1]:
                    stack.pop()
                else :
                    return False
        if len(stack) == 0 :
            return True
        else :
            return False
        