class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = set(["+", "-", "*", "/"])
        for token in tokens:
            #print(stack)
            if token in operations:
                b = stack.pop()
                a = stack.pop()
                res = None
                if token == "+":
                    res = a + b 
                elif token == "-":
                    res = a-b
                elif token == "*":
                    res = a*b
                else :
                    res = int(a/b)
                    #print(res)
                stack.append(res)
            else :
                stack.append(int(token))
        return stack[0]