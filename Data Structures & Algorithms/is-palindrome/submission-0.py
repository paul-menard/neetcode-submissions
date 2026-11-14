class Solution:
    def isPalindrome(self, s: str) -> bool:
        ## first we need to convert to the right format
        new_s = ""
        for c in s :
            if c.isalnum():
                new_s += c.lower()
        print(new_s)
        l = 0 
        r = len(new_s)-1
        while l <= r :
            print(s[l], s[r])
            if new_s[l] != new_s[r] :
                ## not palindrome
                return False
            else : 
                l += 1
                r -= 1 

        return True
        