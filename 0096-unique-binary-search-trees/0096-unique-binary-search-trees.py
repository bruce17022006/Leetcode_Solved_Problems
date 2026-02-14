class Solution:
    def numTrees(self, n: int) -> int:
       c=math.factorial(2*n)
       d=math.factorial(n+1)
       e=math.factorial(n)
       f=c//(d*e)
       if n==0:
        return n
       else:
        return f
       