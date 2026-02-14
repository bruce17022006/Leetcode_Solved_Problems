class Solution:
    def maximum69Number (self, num: int) -> int:
        nums=list(map(int,str(num)))
        for i in range(len(nums)):
            if(nums[i]==6):
                nums[i]=9
                break
        n = int("".join(map(str, nums))) 
        return n