class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        while n>0:
            if n==1:
                return True
            elif n%2==0:
                n/=2
            else:
                return False
            
    n=16
            


    