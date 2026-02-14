class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        import numpy as np
        num=np.square(nums)
        n=len(num)
        result=[0]*n
        left=0
        right=n-1
        index=n-1
        while left<=right:
            left_squared=num[left]
            right_squared=num[right]
            if left_squared>right_squared:
                result[index]=int(left_squared)
                left+=1
            else:
                result[index]=int(right_squared)
                right-=1
            index-=1
        return result


        