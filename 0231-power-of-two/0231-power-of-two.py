class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n>0 and 2**30 % n == 0:
            return True 
        return False
        