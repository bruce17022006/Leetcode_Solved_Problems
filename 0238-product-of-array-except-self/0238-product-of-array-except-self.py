class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final=[1]*len(nums)
        prefix=1
        suffix=1
        for i in range(len(nums)):
            final[i]=prefix
            prefix=prefix*nums[i]
        for i in range(len(nums)-1,-1,-1):
            final[i]=final[i]*suffix
            suffix=suffix*nums[i]
        return final

        