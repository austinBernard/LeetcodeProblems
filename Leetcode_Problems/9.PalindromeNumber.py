class Solution:
    def isPalindrome(self, x: int) -> bool:
        storeX = str(x)
        l = 0
        r = len(storeX) - 1

        while l < r:
            if storeX[l] != storeX[r]:
                return False
            l += 1
            r -= 1
        return True
