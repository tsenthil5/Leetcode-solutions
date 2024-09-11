class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while(n!=1):
            n = n/2
            if n % 1 != 0:
                return False

        return True
        