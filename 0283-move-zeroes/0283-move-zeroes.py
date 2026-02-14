class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        j=i+1
        temp=0
        for _ in range(len(nums)):
            if nums[i]!=0:
                i+=1
            if(j<len(nums)and (nums[i]==0 and nums[j]!=0)):
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                i+=1
                j+=1
            else:
                j+=1
        # return nums
        